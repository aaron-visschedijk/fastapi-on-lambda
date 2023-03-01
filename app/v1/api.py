from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .authentication.dependants import authenticated_user
from .authentication import endpoints as auth
from .protected import endpoints as protected



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
    return {"message": "API v1 is live!"}


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(protected.router, prefix="/protected", tags=["Protected"], dependencies=[Depends(authenticated_user)])