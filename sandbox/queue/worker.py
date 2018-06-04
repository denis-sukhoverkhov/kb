import time

import pika


def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(f" [x] Received {body}")
    time.sleep(body.count('.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
