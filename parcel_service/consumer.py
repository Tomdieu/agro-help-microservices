import json,pika
from tortoise import run_async
from parcel_app.database import initDb
from parcel_app.models import Culture
from asyncio.runners import run

run_async(initDb())

credentials = pika.PlainCredentials("myuser","mypass")
parameters = pika.ConnectionParameters("localhost",5672,"/",credentials)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.queue_declare("parcel",durable=True)
def comsume_messages():


    def callback(ch, method, properties, body):
        print("Recieve message",json.loads(body.decode()))

        message:dict = json.loads(body.decode())

        msg_type:str = message.get('type',None)
        data:dict = message.get('data',None)

        if msg_type == 'culture_created':
            
            run(Culture.create(**data),debug=True)
            print("Culture Created!")

        if msg_type == 'culture_updated':
            id = data.pop('id',None)
            if id:
                Culture.filter(id=id).update(**data)
                print(f"Culture with id={id} updated")


        if msg_type == 'culture_deleted':
            id = data.pop('id',None)
            if id:
                Culture.filter(id=id).delete()
                print(f"Culture with id={id} deleted!")

    channel.basic_consume(queue="parcel",on_message_callback=callback,auto_ack=False)

    print("Start Consuming")
    print("[x] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

comsume_messages()