import pika
from models import Contacts
import time
from mongoengine import *


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')
print(' [*] Waiting for messages. To exit press CTRL+C')


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')
print(' [*] Waiting for messages. To exit press CTRL+C')


def message_processing(body):
    message_len = len(body)
    return(message_len)

def callback(ch, method, properties, body):
    mess = Contacts.objects()
    print(f" Received {body}")
    Contacts.objects(message=False).update_one(set__message=True)
    time.sleep(1)
    lenght = message_processing(body)
    print(f" Done: message lenght: {lenght}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
