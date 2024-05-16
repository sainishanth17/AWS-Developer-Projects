import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    if 'body' in event:
        input = json.loads(event['body'])
        if 'userid' in input \
            and 'firstname' in input \
            and 'lastname' in input \
            and 'department' in input \
            and 'location' in input:
                dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
                table = dynamodb.Table('users')
                try:
                    response = table.put_item(
                        Item={
                            'userid': input['userid'],
                            'FirstName': input['firstname'],
                            'LastName': input['lastname'],
                            'Department': input['department'],
                            'Location': input['location']
                        })
                    
                    return {
                        'statusCode': 200,
                        'body': json.dumps('Record has been successfully inserted')
                    }
                except Exception as e:
                    return {
                        'statusCode': 500,
                        'body': json.dumps({'Error': str(e)})
                    }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({'Error':'Input body not defined'})
        }
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
