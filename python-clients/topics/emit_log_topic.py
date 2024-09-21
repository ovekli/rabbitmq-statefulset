#!/usr/bin/env python

import pika, sys

credentials = pika.PlainCredentials('ehm-user', 'ehm-user')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='test0', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(f" [x] Sent {routing_key}:{message}")
connection.close()