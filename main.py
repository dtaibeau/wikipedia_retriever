from fastapi import FastAPI
import requests
# from pydantic import BaseModel

app = FastAPI()

# class FirstParagraph(BaseModel):
#     """Data model for paragraph segment"""
#     title: str
#     text: str


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Wikipedia Retriever"}


@app.get("/article/{article_name}")
async def get_article(article_name: str):
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{article_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title"),
            "extract": data.get("extract")
        }
    else:
        return {"error": "Article not found"}

