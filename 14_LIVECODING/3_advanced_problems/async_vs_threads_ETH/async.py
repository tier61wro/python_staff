import aiohttp
import asyncio
import time


async def fetch_data(session, url):
    async with session.get(url) as response:
        text = await response.text()
        print(f"Fetched {len(text)} characters from {url}")


async def main():
    urls = [f'https://jsonplaceholder.typicode.com/posts/{i}' for i in range(1, 100)]

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Time taken with asyncio: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
