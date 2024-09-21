#!/usr/bin/env python

import pika, sys

credentials = pika.PlainCredentials('ehm-user', 'ehm-user')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='test0', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Sent {severity}:{message}")
connection.close()