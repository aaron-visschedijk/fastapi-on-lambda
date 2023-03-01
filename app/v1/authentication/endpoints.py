from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from .models import UserAuth, User
from .utils import user_db
from .utils.jwt import create_access_token, create_refresh_token, decode_token, revoke_refresh_token, is_revoked
from .utils.password import verify_password, get_password_hash
from .dependants import authenticated_user


router = APIRouter()


@router.get("")
async def root():
    return {"message": "Auth module is live!"}


@router.get("/test")
async def test():
    return {"message": "Test!"}


@router.post("/signup", summary="Sign up for a new account")
async def signup(data: UserAuth):
    if user_db.get_user_by_email(data.email):
        raise HTTPException(
            status_code=400,
            detail="User with this email already exist"
        )
    user_db.create_user(data)


@router.post("/login", summary="Login to an existing account")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_db.get_user_by_email(form_data.username)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email"
        )
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {
        "access_token": create_access_token(user.email),  
        "refresh_token": create_refresh_token(user.email)
    }


@router.post("/refresh", summary="Refresh access token")
async def refresh(grant_type: str = Form(), refresh_token: str = Form()):

    payload = decode_token(refresh_token, refresh_token=True, verify=True)
    if grant_type != "refresh_token":
        raise HTTPException(
            status_code=400,
            detail="Invalid grant type"
        )
    if is_revoked(refresh_token, payload.exp):
        raise HTTPException(
            status_code=400,
            detail="Invalid refresh token"
        )
    user = user_db.get_user_by_email(payload.sub)
    revoke_refresh_token(refresh_token, payload.exp)
    return {
        "detail": "Access token refreshed",
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email)
    }
    

@router.get("/logout", summary="Logout from an account")
async def logout(refresh_token: str = Form(), user: User = Depends(authenticated_user)):
    revoke_refresh_token(refresh_token, decode_token(refresh_token).exp)
    return {"message": "Logged out successfully"}
