import faker
from models import Contacts
from connection import connection
import pika
from time import sleep
import json
from datetime import datetime



fake = faker.Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='email_exchange', exchange_type='direct')
channel.queue_declare(queue='email_queue')
channel.queue_bind(exchange='email_exchange', queue='email_queue')


def add_data():
    for _ in range (10):
        fake_fullname = fake.name()
        fake_email = fake.email()
        document = Contacts(fullname=fake_fullname, email=fake_email)
        document.save()



def main():

    contacts = Contacts.objects()

    for contact in contacts:
        message = {
            "id": str(contact.id),
            "payload": [contact.fullname, contact.email],
            "date": datetime.now().isoformat(),
            "text": fake.text()
        }

        channel.basic_publish(
            exchange='email_exchange',
            routing_key='email_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print("Sent %r" % message)
        sleep(3)
    connection.close()



if __name__ == "__main__":
    add_data()
    main()