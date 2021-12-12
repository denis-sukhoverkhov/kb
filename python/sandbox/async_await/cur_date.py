import asyncio
import hashlib

import aiohttp


async def fetch(session, url):
    async with session.get(url, verify_ssl=False) as response:
        return await response.text()


async def download_pages(url_list):
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    for url in url_list:
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, url)
            hash = hashlib.md5(html.encode("utf-8"))
            print(hash.hexdigest())
        if (loop.time() + 1.0) >= end_time:
            break


url_list = (
    "https://www.bbc.com/news/world-europe-44932366",
    "https://www.bbc.com/news/world-europe-44948173",
    "https://www.bbc.com/news/world-europe-44935473",
)
asyncio.run(download_pages(url_list))
