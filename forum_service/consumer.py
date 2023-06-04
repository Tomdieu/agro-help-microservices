import json, pika
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forum_service.settings")
django.setup(set_prefix=True)
import traceback
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


def comsume_messages():
    credentials = pika.PlainCredentials("myuser", "mypass")
    parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

    connection = pika.BlockingConnection(parameters=parameters)

    channel = connection.channel()

    channel.queue_declare("forum", durable=True)

    def callback(ch, method, properties, body):
        print("Recieve message", json.loads(body.decode()))
        content_type = properties.content_type
        message: dict = json.loads(body.decode())

        print("Message Recieved ",message)

        msg_type: str = message.get("type", None)
        data: dict = message.get("data", None)

        def create_user(data,ch):
            user_data = data.get("user", None)
            user = User.objects.create(**user_data)
            user_token = data.get("token", None)
            if user_token:
                Token.objects.create(user=user, key=user_token)
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print("User created!")

        def update_user(data,ch):
            user_data:dict = data.get("user", None)
            id = user_data.pop('id',None)
            if id:
                User.objects.filter(id=id).update(**user_data)
                ch.basic_ack(delivery_tag=method.delivery_tag)
                print("User Updated!")

        if msg_type == "user_created":
            try:

                create_user(data,ch)
            except:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        if msg_type == 'user_updated':
            id = data.get("id", None)
            user = data.get('user',None)
            id = user.get('id',None)
            
            if User.objects.filter(id=id).exists():
                update_user(data,ch)
            else:
                create_user(data,ch)
        if msg_type == "user_deleted":
            if data.get("id", None):
                User.objects.filter(id=data.get("id")).delete()
                ch.basic_ack(delivery_tag=method.delivery_tag)
                print("User Deleted!")

    channel.basic_consume(queue="forum", on_message_callback=callback, auto_ack=False)

    print("Start Consuming")
    print("[x] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ =='__main__':
    try:
        comsume_messages()
    except Exception as e:
        traceback.print_exc()
