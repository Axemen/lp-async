import asyncio
from collections import Counter
from datetime import datetime

import aiohttp


async def get(session, url, i):
    async with session.get(url) as response:
        html = await response.text()
        return html, i


async def main(links):
    async with aiohttp.ClientSession() as session:

        tasks = [get(session, link, i) for i, link in enumerate(links)]

        c = Counter()
        for task in asyncio.as_completed(tasks):
            html, i = await task
            c.update(html)

        print(c.most_common(5))


if __name__ == "__main__":
    start = datetime.now()
    links = [
        "https://stackoverflow.com/",
        "https://www.iexcloud.io/",
        "https://www.tiingo.com/",
        "https://docs.python.org/3/",
        "https://github.com/",
        "https://en.wikipedia.org/wiki/Main_Page",
        "https://www.reddit.com/",
        "https://www.youtube.com/",
        "https://aws.amazon.com/",
        "https://azure.microsoft.com/en-us/",
        "http://python-guide.org",
        "http://python-requests.org",
        "https://pandas.pydata.org/",
    ]
    asyncio.run(main(links))
    print("time elapsed", datetime.now() - start)
