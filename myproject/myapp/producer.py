import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_queue')

message = 'Hello, world!'
channel.basic_publish(exchange='', routing_key='my_queue', body=message)

print("Message sent: %s" % message)

connection.close()
