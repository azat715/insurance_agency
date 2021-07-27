import pika
import signal


def signal_handler(signal, frame):
    print("стоп контейнера")
    connection.close()
    sys.exit(0)


def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    parameters = pika.ConnectionParameters("rabbitmq", credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="test")
    channel.basic_consume("test", on_message)

    channel.start_consuming()
    signal.signal(signal.SIGTERM, signal_handler)


if __name__ == "__main__":
    main()
