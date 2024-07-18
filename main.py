from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

class FirstParagraph(BaseModel):
    """Data model for Wikipedia article's first paragraph"""
    title: str
    paragraph: str

@app.get("/")
async def read_root():
    """
    Root endpoint returning a welcome message.

    Returns:
        dict: welcome message
    """
    return {"message": "Welcome to the Wikipedia Retriever"}

@app.get("/article/{article_name}", response_model=FirstParagraph)
async def get_article(article_name: str):
    """
    Endpoint to fetch the first paragraph of a Wikipedia article.

    Args:
        article_name (str): name of wiki article

    Returns:
        FirstParagraph: A structured response containing title and first paragraph of the article if found,
              otherwise raises HTTP exception 
    """
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{article_name}'
    response = requests.get(url)
    if response.status_code == 200: # if successful
        data = response.json()
        return FirstParagraph(
            title=data.get("title"),
            paragraph=data.get("extract") or "No extract available for this article."
        )
    else:
        raise HTTPException(status_code=404, detail="Article not found")

