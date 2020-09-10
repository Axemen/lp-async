import asyncio
import json
import os

import websockets
from dotenv import load_dotenv
import numpy as np

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

    values = []

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps(subscribe))

        print("Connected!")

        async for message in ws:
            data = json.loads(message)
            try:
                if data['data'][1] == 'btcusd':
                    print(data['data'])

                    # values.append(data['data'][-1])
                    # if len(values) > 10:
                    #     values.pop(0)

                    # print(sum(values) / len(values))
                
            except KeyError:
                pass
            # await asyncio.sleep(.05)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(listen())
