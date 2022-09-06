"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from loguru import logger
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:  # type: aiohttp.ClientResponse
        data = await response.json()
        return data


async def fetch_users_data() -> str:
    logger.info("fetch users")

    # # session = aiohttp.ClientSession()
    # # session.get(...)
    # # await session.close()
    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, USERS_DATA_URL)
        logger.info("done for service {}", USERS_DATA_URL)
        return data


async def fetch_posts_data() -> str:
    logger.info("fetch user {}", POSTS_DATA_URL)

    # # session = aiohttp.ClientSession()
    # # session.get(...)
    # # await session.close()
    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, POSTS_DATA_URL)
        logger.info("done for service {}", POSTS_DATA_URL)
        return data