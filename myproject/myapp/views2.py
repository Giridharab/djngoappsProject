from django.http import HttpResponse
import pika
from django.conf import settings


def send_message(request):
    message = "Hello, world!"
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            virtual_host=settings.RABBITMQ_VIRTUAL_HOST,
            credentials=pika.PlainCredentials(
                settings.RABBITMQ_USERNAME, settings.RABBITMQ_PASSWORD
            ),
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")
    channel.basic_publish(exchange="", routing_key="my_queue", body=message)
    connection.close()
    return HttpResponse("Message sent: " + message)
