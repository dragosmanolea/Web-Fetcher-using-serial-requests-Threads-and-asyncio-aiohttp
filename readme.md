Great example of using asyncio and threads in Python.
In this example, you can find 3 implementations for fetching data from internet:
    - using serial requests
    - using threads
    - using asyncio and aiohttp

On my M1 Mac, for 5 urls, I reduced the running time from ~ 3 seconds from serial method to 0.9s - 1s using Threads and asyncio implementation.