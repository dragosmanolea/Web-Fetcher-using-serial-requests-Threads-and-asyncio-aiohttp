import logging
import threading
import time
import requests
from urllib.parse import urlparse

def get_data(url):
    print(f"Fetching data for: {url}")
    data = requests.get(url)
    with open(f"{urlparse(url).netloc}.txt", "w+") as opened_file:
        opened_file.write(data.text)

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/",
        "https://www.google.com/",
        "https://www.olx.ro/",
        "https://www.facebook.com/",
        "https://www.instagram.com/"
    ]
    current = time.time()
    for url in urls:
        x = threading.Thread(target=get_data, args=(url,))
        x.start()
    print(time.time() - current)
