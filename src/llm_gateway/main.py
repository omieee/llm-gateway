import typing

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> typing.Any:
    return {"message": "Hello World"}


@app.get("/hello")
async def hello() -> typing.Any:
    return {"response": "Static Response"}
