import pika
from django.conf import settings


RABBITMQ_SERVER = settings.RABBITMQ["SERVER"]
USER = settings.RABBITMQ["USER"]
PASS = settings.RABBITMQ["PASS"]
RABBITMQ_QUEUE = settings.RABBITMQ["QUEUE"]
ROUTING_KEY = RABBITMQ_QUEUE


class Producer:
    """Отправка сообщений в брокер"""

    def __init__(self) -> None:
        credentials = pika.PlainCredentials(USER, PASS)
        parameters = pika.ConnectionParameters(RABBITMQ_SERVER, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=RABBITMQ_QUEUE)

    def publish(self, msg):
        self.channel.basic_publish(exchange="", routing_key=ROUTING_KEY, body=msg)

    def close(self):
        self.connection.close()
