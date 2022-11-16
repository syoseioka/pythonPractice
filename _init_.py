import json

def common(message):
    data = json.loads(message)
    json_message = json.dumps(data, indent=2)
    return json_message

def s3():
    message = '{"ServiceName": "Amazon S3"}'
    return common(message)

def dynamodb():
    message = '{"ServiceName": "Amazon DynamoDB"}'
    return common(message)

def greengrass():
    message = '{"ServiceName": "AWS IoT Greengrass"}'
    return common(message)