import asyncio
import aiohttp
import time
from urllib.parse import urlparse

urls = [
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://www.olx.ro/",
    "https://www.facebook.com/",
    "https://www.instagram.com/"
]

async def get_data(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            with open(f"{urlparse(url).netloc}.txt", "w+") as opened_file:
                opened_file.write(text)
    except Exception as e:
        print(str(e))

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(f"Fetching data for: {url}")
            tasks.append(get_data(session, url))
        await asyncio.gather(*tasks)

current = time.time()
asyncio.run(main())
print(time.time() - current)
