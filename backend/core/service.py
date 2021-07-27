import pika


class Producer:
    """Отправка сообщений в брокер"""

    def __init__(self) -> None:
        credentials = pika.PlainCredentials("guest", "guest")
        parameters = pika.ConnectionParameters("rabbitmq", credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="test")

    def publish(self, msg):
        self.channel.basic_publish(exchange="", routing_key="test", body=msg)

    def close(self):
        self.connection.close()
