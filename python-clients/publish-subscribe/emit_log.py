#!/usr/bin/env python

import pika, sys

credentials = pika.PlainCredentials('ehm-user', 'ehm-user')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='test0', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()