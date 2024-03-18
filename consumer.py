import connect
from models import Contact

import os
import sys

import pika

#  Заглушка для відправлення email
def send_email(adr_):
    print(f"Send Email to {adr_}")


def main():
    # Створення з'єднання з RabbitMQ
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )
    channel = connection.channel()
    queue_name = "hw8_que"
    channel.queue_declare(queue=queue_name, durable=True)

    # Отримання даних з черги, виклих ф-ції заглушки, та зміна стану поля Contact з False на True
    def callback(ch, method, properties, body):
        pk = body.decode()
        task = Contact.objects(id=pk, completed=False).first()
        if task:
            send_email(task.name)
            task.update(set__completed=True)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
