import boto3
import json
import base64

import config

BUCKET_NAME = 'detections'


def upload(filename, data):
    s3 = boto3.resource(
        's3',
        endpoint_url=config.S3_ENDPOINT,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
    )
    s3.Object(BUCKET_NAME, filename).put(Body=str(data))


def handle(body):
    # print 'recieved message: ' + body
    data = json.loads(body)
    img_data = base64.b64decode(data['body']['detection']['frame_content'])
    filename = data['body']['user_info']['key'] + '-' + data['body']['detection']['timestamp'] + '.png'
    upload(filename, data)
