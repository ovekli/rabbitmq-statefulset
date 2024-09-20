#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='ehm-broker'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")