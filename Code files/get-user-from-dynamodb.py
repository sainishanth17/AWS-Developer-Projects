import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    print(event)
    try:
            userid = event['pathParameters']['userid']
    except Exception as e:
        return {
            'statusCode':500,
            'body': json.dumps({'Error':'No User ID defined in the input'})
        }
    
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    
    table = dynamodb.Table('users')
    try:
        response = table.get_item(
            Key={
                'userid':userid
            }
        )
        if 'Item' in response:
            return {
                'statusCode':200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode':404,
                'body': json.dumps({'Error':'No user found for given ID'})
            }
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode':500,
            'body': json.dumps({'Error':'Error getting user information'})
                }
