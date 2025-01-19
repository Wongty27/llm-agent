# from typing import AsyncGenerator
# from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

# client = AsyncIOMotorClient("")

# async def get_session() -> AsyncGenerator[AsyncIOMotorClientSession | None]:
#     async with await client.start_session() as session:
#         yield session