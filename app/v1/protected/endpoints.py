from fastapi_lambda_router import LambdaRouter

router = LambdaRouter()

@router.get("/")
async def root():
    return {"message": "Protected API is live!"}