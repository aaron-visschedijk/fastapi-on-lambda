from fastapi import APIRouter, HTTPException, status
from ..utils import database

router = APIRouter()

@router.get("/user/{id}")
def get_user(id: str):
    user = database.get_user(id)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
@router.get("/user/email/{email}")
def get_user_by_email(email: str):
    user = database.get_user_by_email(email)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")