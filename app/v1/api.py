from fastapi import Depends
from .authentication.dependants import authenticated_user
from .authentication import endpoints as auth
from .protected import endpoints as protected
from lambdarouter_aaron_visschedijk.router import LambdaRouter



prefix = "/v1"

router = LambdaRouter()


@router.get("/")
async def root():
    return {"message": "API v1 is live!"}


router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(protected.router, prefix="/protected", tags=["Protected"], dependencies=[Depends(authenticated_user)])