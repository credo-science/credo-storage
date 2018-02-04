import os

RMQ_HOST = os.environ['RMQ_HOST'] if 'RMQ_HOST' in os.environ.keys() else 'localhost'

S3_ENDPOINT = os.environ['S3_ENDPOINT'] if 'S3_ENDPOINT' in os.environ.keys() else 'https://storage.cloud.cyfronet.pl'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID'] if 'AWS_ACCESS_KEY_ID' in os.environ.keys() else ''
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'] if 'AWS_SECRET_ACCESS_KEY' in os.environ.keys() else ''
