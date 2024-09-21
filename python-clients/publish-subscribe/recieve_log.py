#!/usr/bin/env python

import pika, sys

credentials = pika.PlainCredentials('ehm-user', 'ehm-user')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='test0', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()