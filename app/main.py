from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import v1.api as api_v1

app = FastAPI()


origins = [
    "http://localhost:3000",
    "https://ypp3d3jsvjj3unimeewvydwqyy0iludg.lambda-url.eu-central-1.on.aws/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "API is live!"}

@app.get("/health")
async def health():
    return {"message": "API is healthy!"}

app.include_router(api_v1.router, prefix=api_v1.prefix)

handler = Mangum(app)