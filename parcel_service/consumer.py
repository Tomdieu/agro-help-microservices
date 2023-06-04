import json, pika
from tortoise import run_async, Tortoise
from parcel_app.database import initDb
from parcel_app.models import Culture, User, Token
import asyncio
import traceback

from parcel_app.conf import RABBITMQ_HOST

mainloop = asyncio.get_event_loop()
mainloop.run_until_complete(initDb())


# asyncio.run(initDb())
def comsume_messages():
    asyncio.run(initDb(), debug=True)

    credentials = pika.PlainCredentials("myuser", "mypass")
    parameters = pika.ConnectionParameters(RABBITMQ_HOST, 5672, "/", credentials)

    connection = pika.BlockingConnection(parameters=parameters)

    channel = connection.channel()

    channel.queue_declare("parcel", durable=True)

    def callback(ch, method, properties, body):
        print("Recieve message", json.loads(body.decode()))
        content_type = properties.content_type
        message: dict = json.loads(body.decode())

        msg_type: str = message.get("type", None)
        data: dict = message.get("data", None)

        async def create_user(data, ch):
            user_data: dict = data.get("user", None)
            user_data.pop("password", None)
            if user_data is not None:
                print("user_data", user_data)
                user = await User.create(**user_data)
                user_token = data.get("token", None)
                if user_token is not None:
                    await Token.create(user=user, key=user_token)
                print("User Created")
                ch.basic_ack(delivery_tag=method.delivery_tag)

        async def updated_user(data, ch):
            user_data: dict = data.get("user", None)
            id = user_data.pop("id", None)
            if id:
                await User.filter(id=id).update(**user_data)
                print("User Updated")
                ch.basic_ack(delivery_tag=method.delivery_tag)

        async def create_or_updated(data: dict, ch):
            id = data.get("id", None)
            user = User.filter(id=id)
            if user.exists():
                updated_user(data, ch)
            else:
                create_user(data, ch)

        if msg_type == "culture_created":

            async def created_culture(data):
                await Culture.create(**data)

            asyncio.run(created_culture(data))
            print("Culture Created!")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        if msg_type == "culture_updated":
            user = data.get('user',None)
            id = user.get('id',None)
            
            if id:
                Culture.filter(id=id).update(**data)
                print(f"Culture with id={id} updated")
                ch.basic_ack(delivery_tag=method.delivery_tag)

        if msg_type == "culture_deleted":
            id = data.pop("id", None)
            if id:
                Culture.filter(id=id).delete()
                print(f"Culture with id={id} deleted!")
                ch.basic_ack(delivery_tag=method.delivery_tag)

        if msg_type == "user_created":
            user: dict = data.get("user", None)
            if user:
                asyncio.run(create_user(data, ch))

        if msg_type == "user_updated":
            user: dict = data.get("user", None)
            if user:
                asyncio.run(create_or_updated(data, ch))

        if msg_type == "user_deleted":

            async def delete_user(id):
                await User.filter(id=id).first().delete()
                print("User Deleted")
                ch.basic_ack(delivery_tag=method.delivery_tag)

            if data.get("id", None):
                asyncio.run(delete_user(data.get("id")), debug=True)

    channel.basic_consume(queue="parcel", on_message_callback=callback, auto_ack=False)

    print("Start Consuming")
    print("[x] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


try:
    # run_async(initDb())
    comsume_messages()
except Exception as e:
    traceback.print_exc()
finally:

    async def close_conn():
        await Tortoise.close_connections()

    mainloop.run_until_complete(close_conn())

    mainloop.close()
