import os
from fastapi import Depends, HTTPException
from datetime import datetime, timezone, timedelta
from typing import Union, Any
import jwt
from ..models import RevokedToken, TokenPayload
from pydantic import ValidationError
import boto3

ACCESS_TOKEN_EXPIRE_SECONDS = 10
REFRESH_TOKEN_EXPIRE_SECONDS = 30
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'secret')
JWT_REFRESH_SECRET_KEY = os.environ.get('JWT_REFREH_SECRET_KEY', 'secret')


db_client = boto3.resource(service_name='dynamodb', region_name='eu-central-1')
table = db_client.Table("jwt_denylist")


def create_access_token(subject: Union[str, Any]) -> str:
    exp = datetime.now(tz=timezone.utc) + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    payload = {"exp": exp, "sub": str(subject)}
    encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any]) -> str:
    exp = datetime.now(tz=timezone.utc) + timedelta(seconds=REFRESH_TOKEN_EXPIRE_SECONDS)
    payload = {"exp": exp, "sub": str(subject)}
    encoded_jwt = jwt.encode(payload, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
    

def revoke_refresh_token(token: str, exp: int):
    to_revoke = RevokedToken(jwt=token, exp=exp)
    table.put_item(Item=to_revoke.dict())
        

def is_revoked(token: str, exp: int) -> bool:
    response = table.get_item(Key={"jwt": token, "exp": exp})
    if response.get('Item'):
        return True
    else:
        return False


def decode_token(token: str, verify: bool = True, refresh_token: bool = False) -> TokenPayload:
    try:
        key = JWT_REFRESH_SECRET_KEY if refresh_token else JWT_SECRET_KEY
        payload = jwt.decode(
            token, key, algorithms=[ALGORITHM], options={"verify_exp": verify}
        )
        token_data = TokenPayload(**payload)
        return token_data
    except (jwt.exceptions.ExpiredSignatureError, ValidationError):
        raise HTTPException(status_code=401, detail="Invalid token")


def verify_token(token: str, refresh_token: bool = False):
    token_data = decode_token(token, verify=False, refresh_token=refresh_token)
    
    if token_data.exp < int(datetime.now(tz=timezone.utc).timestamp()):
        raise HTTPException(status_code=401, detail="Token expired")