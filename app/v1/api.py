from fastapi import APIRouter, Depends
from .authentication.dependants import authenticated_user
from .authentication import endpoints as auth
from .protected import endpoints as protected


prefix = "/v1"

router = APIRouter()


@router.get("")
async def root():
    return {"message": "API v1 is live!"}


router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(protected.router, prefix="/protected", tags=["Protected"], dependencies=[Depends(authenticated_user)])