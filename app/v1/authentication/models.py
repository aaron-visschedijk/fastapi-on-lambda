from pydantic import BaseModel, EmailStr

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: str
    email: EmailStr
    password: str

class TokenPayload(BaseModel):
    sub: str
    exp: int

class RevokedToken(BaseModel):
    jwt: str
    exp: int