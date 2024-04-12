import os

from google.cloud import pubsub_v1

credentials_path = r'C:\Users\josuv\OneDrive\Escritorio\Universidad\Quinto Semestre\ArquiSoft\Sprint 2\Banco\banco\banco\logic\requests-messages_privatekey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


def publish_phone_number(phone_number):

    publisher = pubsub_v1.PublisherClient()
    topic_path = 'projects/pub-sub-messages/topics/requests-messages'

    data = 'numero del cliente'
    data = data.encode('utf-8')
    attributes = {
    'phone': phone_number
    }

    future = publisher.publish(topic_path, data,**attributes)