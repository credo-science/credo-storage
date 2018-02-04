import pika

import config
from handler import handle

QUEUE_NAME = 'detections_save'


def callback(ch, method, properties, body):
    try:
        handle(body)
    except Exception, e:
        print "Error processing message " + str(e)

    # ack anyway to prevent message buildup
    ch.basic_ack(delivery_tag=method.delivery_tag)


def listen():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    print "waiting for messages"

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback, queue=QUEUE_NAME)

    channel.start_consuming()


if __name__ == '__main__':
    listen()
