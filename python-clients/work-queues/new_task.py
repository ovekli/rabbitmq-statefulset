#!/usr/bin/env python

import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='ehm-broker'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode = pika.DeliveryMode.Persistent
                      ))
print(f" [x] Sent {message}")