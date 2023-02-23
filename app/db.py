import boto3

db_client = boto3.resource(service_name='dynamodb', region_name='eu-central-1')
table = db_client.Table("users")

def query(user_id):
    response = table.get_item(Key={'id': user_id})
    return response['Item']

def create_user(user_id, email):
    table.put_item(
        Item={
            'id': user_id,
            'email': email
        }
    )