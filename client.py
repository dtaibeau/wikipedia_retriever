import httpx
import asyncio
import streamlit

async def fetch_wikipedia_article(article_name):
    """
    Fetch the first paragraph of a Wikipedia article from the FastAPI server.

    Args:
        article_name (str): The name of the Wikipedia article.

    Returns:
        dict: The JSON response from the FastAPI server containing the title and paragraph.
    """
    print(f"fetching article: {article_name}")
    url = f"http://127.0.0.1:8000/article/{article_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    print(f"received response with status code: {response.status_code}")
    if response.status_code == 200:
        print("success! parsing response")
        return response.json()
    else:
        print("error: Article not found.")
        return {"error": "Article not found"}

async def main():
    article_name = "Never_Gonna_Give_You_Up"
    result = await fetch_wikipedia_article(article_name)
    print(result)

async def main():
    st.title("Wikipedia Article Retriever")
    article_name = st.text_input("Enter Wikipedia Article Name")
    if st.button("Fetch Article"):
        if article_name:
            result = await fetch_wikipedia_article(article_name)
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Title: {result['title']}")
            st.write(result['paragraph'])
    else:
        st.error("Please enter an article name.")

if __name__ == "__main__":
    asyncio.run(main())