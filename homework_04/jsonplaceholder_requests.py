"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:  # type: aiohttp.ClientResponse
        data = await response.json()
        return data


async def get_user_data() -> str | None:
    # logger.info("fetch user {}", service.name)
    #
    # # session = aiohttp.ClientSession()
    # # session.get(...)
    # # await session.close()
    # async with aiohttp.ClientSession() as session:
    #     data: dict = await fetch_json(session, service.url)
    #     logger.info("done for service {}", service.name)
    #     return data.get(service.field)
    pass


async def get_posts_data() -> str | None:
    # logger.info("fetch user {}", service.name)
    #
    # # session = aiohttp.ClientSession()
    # # session.get(...)
    # # await session.close()
    # async with aiohttp.ClientSession() as session:
    #     data: dict = await fetch_json(session, service.url)
    #     logger.info("done for service {}", service.name)
    #     return data.get(service.field)
    pass