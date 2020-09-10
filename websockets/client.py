import websockets
import asyncio

import numpy as np
import pandas as pd

numbers = []

async def listen():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        async for message in ws:
            print(message)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(listen())