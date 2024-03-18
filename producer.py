import connect

from models import Contact
import faker

import pika

# Встановлення локалі для випадкових даних
fake_data = faker.Faker("uk_UA")

# Створення з'єднання з RabbitMQ
credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

exchange = "hw8_ex"
queue_name = "hw8_que"

channel.exchange_declare(exchange=exchange, exchange_type="direct")
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange, queue=queue_name)

# Створення колекції Contact з даними, та передаєм ObjectID в чергу
def create_tasks(nums: int):
    for i in range(nums):
        task = Contact(
            name=fake_data.unique.name(), email=fake_data.unique.email()
        ).save()

        channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=str(task.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()


if __name__ == "__main__":
    create_tasks(10)
