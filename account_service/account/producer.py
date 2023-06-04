import pika, json

from django.conf import settings
# parameters = pika.URLParameters('amqps://krimticf:rb_pr0-RABLjrHtEvKYUCa7lfQtMi8hG@jaragua.lmq.cloudamqp.com/krimticf')

# connection = pika.BlockingConnection(parameters)


def publish(method, body):
    try:
        credentials = pika.PlainCredentials("myuser", "mypass")
        parameters = pika.ConnectionParameters(settings.RABBITMQ_HOST, 5672, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        data: dict = {"type": method, "data": body}
        properties = pika.BasicProperties(method)
        channel.basic_publish(
            exchange="",
            routing_key="parcel",
            body=json.dumps(data),
            properties=properties,
        )
        channel.basic_publish(
            exchange="",
            routing_key="forum",
            body=json.dumps(data),
            properties=properties,
        )

        print("Message Send successfully")
    except pika.exceptions.AMQPConnectionError:
        print("Could Not Connect to the RabbitMq Server")
