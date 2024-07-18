# Wikipedia Retriever

This project uses FastAPI to fetch the first paragraph of Wikipedia articles based on a given article name.

## Features

- Fetches the first paragraph of any Wikipedia article
- Uses FastAPI for building the web server
- Asynchronous HTTP requests using httpx
- Data validation using Pydantic

## Requirements

- [FastAPI](https://fastapi.tiangolo.com) for the web framework
- [httpx](https://www.python-httpx.org) for asynchronous HTTP requests
- [Pydantic](https://pydantic-docs.helpmanual.io) for data validation
- [Poetry](https://python-poetry.org) for dependency management

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/wikipedia-retriever.git
    cd wikipedia-retriever
    ```

2. **Install Poetry if you haven't already:**
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install the dependencies:**
    ```bash
    poetry install
    ```

## Usage

1. **Activate the virtual environment:**
    ```bash
    poetry shell
    ```

2. **Run the FastAPI server:**
    ```bash
    poetry run uvicorn main:app --reload
    ```

3. **Test the FastAPI server:**
    - Open your web browser and go to `http://127.0.0.1:8000/article/any-article-name`
    - Or use curl:
      ```bash
      curl http://127.0.0.1:8000/article/any-article-name
      ```

## Project Structure

```plaintext
├── README.md                # Project README file
├── pyproject.toml           # Poetry configuration file
├── poetry.lock              # Poetry lock file
├── .gitignore               # Git ignore file
├── main.py                  # FastAPI server script
├── client.py                # Script to fetch and print Wikipedia articles
```

# How to Contribute
- Fork the repository:
```bash
git clone https://github.com/yourusername/wikipedia-retriever.git
cd wikipedia-retriever
```
- Create your feature branch:
```bash
git checkout -b feature/awesome_feature
```
- Commit your changes:
```bash
git commit -m 'Add feature'
```
- Push to branch:
```bash
git push origin feature/awesome_feature
```
- Open a pull request: Go to the forked repository on GitHub and click on the "New Pull Request" button!

:-)