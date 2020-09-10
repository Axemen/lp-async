from collections import Counter
from datetime import datetime

from requests import get

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

    c = Counter()
    for link in links:
        print("Fetching", link)
        html = get(link).content.decode("utf-8")
        c.update(html)

    # print(num_links)
    print("time elapsed", datetime.now() - start)
