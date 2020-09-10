import websockets
import asyncio
from dotenv import load_dotenv
import os

import json

load_dotenv()


async def listen():
    uri = "wss://api.tiingo.com/crypto"

    subscribe = {
        'eventName': 'subscribe',
        'authorization': os.getenv("TIINGO_KEY"),
        'eventData': {
            'thresholdLevel': 5
        }
    }

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps(subscribe))
        async for message in ws:
            data = json.loads(message)
            try:
                if data['data'][1] == 'btcusd':
                    print(data['data'])
            except:
                pass
        # print("Connected")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(listen())
