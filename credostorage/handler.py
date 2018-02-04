import boto3
import json
import uuid
import base64

import config

BUCKET_NAME = 'detections'
s3 = boto3.resource(
    's3',
    endpoint_url=config.S3_ENDPOINT,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
)


def upload(filename, data):
    s3.Object(BUCKET_NAME, filename).put(Body=str(data))
    print 'successful upload ' + filename


def handle(body):
    # print 'recieved message: ' + body
    data = json.loads(body)
    img_data = base64.b64decode(data['body']['detection']['frame_content'])
    upload(str(uuid.uuid4()) + ".png", data)
