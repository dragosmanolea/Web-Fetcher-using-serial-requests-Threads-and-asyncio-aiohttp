import asyncio
import requests
from urllib.parse import urlparse
import time

def get_data(url):
    print(f"INCEP PENTRU {url}")
    data = requests.get(url)
    with open(f"{urlparse(url).netloc}.txt", "w+") as opened_file:
        opened_file.write(data.text)

urls = [
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://www.olx.ro/",
    "https://www.facebook.com/",
    "https://www.instagram.com/"
]

current = time.time()

for url in urls:
    get_data(url)

print(time.time() - current)
