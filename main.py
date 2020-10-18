import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def start_project(string):
    print(string)


if __name__ == '__main__':
    start_project('Hello World')
