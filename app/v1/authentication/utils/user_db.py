import boto3
from boto3.dynamodb.conditions import Key
from ..models import User, UserAuth
from uuid import uuid4
from .password import get_password_hash

db_client = boto3.resource(service_name='dynamodb', region_name='eu-central-1')
table = db_client.Table("users")


def get_user(user_id: str) -> User:
    response = table.get_item(Key={"id": user_id})
    user_dict = response.get('Item')
    if user_dict:
        return User.parse_obj(user_dict)
    else:
        return None


def get_user_by_email(email: str) -> User:
    response = table.query(
        IndexName="email-index",
        KeyConditionExpression=Key("email").eq(email)
    )
    if response.get('Items'):
        user_dict = response.get('Items')[0]
        return User.parse_obj(user_dict)
    else:
        return None


def create_user(data: UserAuth) -> User:
    id = str(uuid4())
    user = User(id=id, email=data.email, password=get_password_hash(data.password))
    table.put_item(Item=user.dict())
    return user
