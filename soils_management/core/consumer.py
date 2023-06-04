from .models import Culture
import os
import pika
import json
import django


credentials = pika.PlainCredentials("myuser", "mypass")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

# parameters = pika.URLParameters(
#     "amqps://krimticf:rb_pr0-RABLjrHtEvKYUCa7lfQtMi8hG@jaragua.lmq.cloudamqp.com/krimticf"
# )

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue="soil", durable=True)


def callback(ch, method, properties, body):
    print("Recieve in culture")

    rabbitMQMsg: dict = json.loads(body.decode())

    print("Message Recieved ", rabbitMQMsg)

    data: Culture = rabbitMQMsg.get("data", {})
    content_type: str = rabbitMQMsg.get("type", None)

    if content_type == "culture_created":
        Culture.objects.create(**data)

        print("[*] Culture Created %r" % body)

    if content_type == "culture_updated":
        culture = Culture.objects.get(id=data.id)
        culture.name = data.name
        culture.image = data.image
        culture.save()
        print("[*] Culture Updated %r" % body)

    if content_type == "culture_deleted":
        Culture.objects.get(id=data.id).delete()
        print("[*] Culture Deleted %r" % body)


channel.basic_consume(queue="soil", on_message_callback=callback, auto_ack=True)


print("Start Consuming")
print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
