import boto3

db_client = boto3.resource('dynamodb')
table = db_client.Table("users")

def query(user_id):
    response = table.get_item(
        Key={
            'user_id': "1"
        }
    )
    return response
