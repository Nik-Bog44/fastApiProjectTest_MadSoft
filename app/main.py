import uvicorn
from fastapi import FastAPI

from app.routers import memes

app = FastAPI()

app.include_router(memes.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)