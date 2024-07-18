from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Wikipedia Retriever"}


@app.get("/article/{article_name}")
async def get_article(article_name: str):
    return {"article_name": article_name}
