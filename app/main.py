from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import v1.api as api_v1

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is live!"}

@app.get("/health")
async def health():
    return {"message": "API is healthy!"}

app.include_router(api_v1.router, prefix=api_v1.prefix)

handler = Mangum(app)