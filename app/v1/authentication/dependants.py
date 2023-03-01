from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .utils.jwt import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def authenticated_user(token: str = Depends(oauth2_scheme)):
    verify_token(token)