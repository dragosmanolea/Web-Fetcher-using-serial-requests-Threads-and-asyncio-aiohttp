Great example of using asyncio and threads in Python.
In this example, you can find 3 implementations for fetching data from internet:
    1. using serial requests
    2. using threads
    3. using asyncio and aiohttp

On my M1 Mac, for 5 urls, I reduced the running time from ~3 seconds from serial method to 0.9s - 1s using Threads or asyncio implementation.

What happends if I have more urls? Which implementation is better?