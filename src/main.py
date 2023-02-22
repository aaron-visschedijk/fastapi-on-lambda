from fastapi import FastAPI
from mangum import Mangum
from recipe_scrapers import scrape_me
from recipe_scrapers._exceptions import WebsiteNotImplementedError
from base64 import b64decode, binascii
import db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/recipe/{recipe_url_b64}")
async def read_recipe(recipe_url_b64):
    try:
        recipe_url = b64decode(recipe_url_b64).decode('utf-8')
        scraper = scrape_me(recipe_url)
        return scraper.to_json()
    except binascii.Error:
        return "Wrong encoding format"
    except WebsiteNotImplementedError:
        return "Recipe not found!"

@app.get("/user/{user_id}")
async def get_user(user_id):
    return db.query(user_id)

handler = Mangum(app)