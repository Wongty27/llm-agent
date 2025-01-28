import os
from dotenv import load_dotenv
from fastapi import FastAPI
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

load_dotenv("../.env")

async def get_session() -> AsyncGenerator[AsyncIOMotorClientSession | None]:
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    async with await client.start_session() as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    print("Connected to MongoDB")
    try:
        yield
    finally:
        client.close()
        print("Disconnected from MongoDB")

app = FastAPI(
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000, reload=True)