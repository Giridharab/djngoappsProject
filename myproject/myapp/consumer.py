import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_queue')


def callback(ch, method, properties, body):
    print("Received message: %s" % body)


channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

print("Waiting for messages...")
channel.start_consuming()
