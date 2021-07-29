import signal
import json
from os import environ

import pika
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, PlainTextContent

env = environ
RABBITMQ_SERVER = env["RABBITMQ_SERVER"]
USER = env["RABBITMQ_USER"]
PASS = env["RABBITMQ_PASS"]
RABBITMQ_QUEUE = env["RABBITMQ_QUEUE"]

SENDGRID_API_KEY = env["SENDGRID_API_KEY"]
DEFAULT_FROM_EMAIL = env["DEFAULT_FROM_EMAIL"]


def signal_handler(signum, frame):
    """при остановке контейнера, реагирует на SIGTERM docker'а"""
    print("Signal handler called with signal", signum)
    print("стоп контейнера")
    connection.close()
    sys.exit(0)


def on_message(channel, method_frame, _, body):
    """callback отправка письма

    body -- json формата {
        "seller": {"email": seller.email},
        "product": {"name": product.name},
        "customer": {
            "name": instance.name,
            "email": instance.email,
            "telephone": instance.telephone,
        },
    }
    """
    data = json.loads(body)
    product_name = data["product"]["name"]
    customer = data["customer"]
    message = Mail(
        from_email=DEFAULT_FROM_EMAIL,
        to_emails=data["seller"]["email"],
        subject="Вам пришел отклик от клиета",
        plain_text_content=PlainTextContent(
            f"""Дорогой клиент \n
        Ваш товар {product_name} хочет купить клиент \n
        Данные клиента: \n
        {customer["name"]}, \n
        {customer["email"]}, \n
        {customer["telephone"]},"""
        ),
    )
    try:
        sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
        response = sendgrid_client.send(message)
        print(response.status_code)
    except Exception as e:
        print("SendGrid Error:")
        print(e)
    else:
        """channel.basic_ack отправка подтверждения в брокер"""
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def main():
    """запуск consumer"""
    credentials = pika.PlainCredentials(USER, PASS)
    parameters = pika.ConnectionParameters(RABBITMQ_SERVER, credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)  # объявление очереди
    channel.basic_consume(RABBITMQ_QUEUE, on_message)

    channel.start_consuming()
    signal.signal(signal.SIGTERM, signal_handler)


if __name__ == "__main__":
    main()
