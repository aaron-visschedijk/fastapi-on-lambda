from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .utils.jwt import verify_token


token_url = "v1/auth/login"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)


def authenticated_user(token: str = Depends(oauth2_scheme)):
    verify_token(token)