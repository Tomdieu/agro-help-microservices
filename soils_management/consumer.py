import os
import pika
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soils_management.settings")
django.setup()

from django.conf import settings

from core.models import Culture

credentials = pika.PlainCredentials("myuser", "mypass")
parameters = pika.ConnectionParameters(settings.RABBITMQ_HOST, 5672, "/", credentials)

# parameters = pika.URLParameters(
#     "amqps://krimticf:rb_pr0-RABLjrHtEvKYUCa7lfQtMi8hG@jaragua.lmq.cloudamqp.com/krimticf"
# )

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue="soil")


def callback(ch, method, properties, body):
    print("Recieve in culture")


    content_type = properties.content_type
    message: dict = json.loads(body.decode())

    msg_type: str = message.get("type", None)
    data: dict = message.get("data", None)

    if msg_type == "culture_created":
        Culture.objects.create(**data)
        print("Culture Created!")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    if msg_type == "culture_updated":
        id = data.pop("id", None)
        Culture.objects.filter(id=id).update(**data)
        print(f"Culture with id={id} updated!")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    if msg_type == "culture_deleted":
        id = data.pop("id", None)
        if id:
            Culture.objects.filter(id=id).delete()
            print(f"Culture with id={id} deleted!")
            ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue="soil", on_message_callback=callback, auto_ack=True)


print("Start Consuming")
print(" [x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
