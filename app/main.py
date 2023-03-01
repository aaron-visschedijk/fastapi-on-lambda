from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from mangum import Mangum
import v1.api as api_v1

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    app.openapi_schema = get_openapi(
        title="FastAPI on AWS Lambda",
        version="1.0.0",
        description="[API v1 docs](/v1/docs)",
        routes=app.routes,
    )
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
async def root():
    return {"message": "API is live!"}

app.mount("/v1", api_v1.app)

handler = Mangum(app)