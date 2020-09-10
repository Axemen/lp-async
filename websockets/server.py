import asyncio
import random
import signal

import websockets

signal.signal(signal.SIGINT, signal.SIG_DFL)

async def random_numbers(ws, path):
    while True:
        n = random.randint(0, 10)
        print(n)
        await ws.send(str(n))
        await asyncio.sleep(.2)

start_server = websockets.serve(random_numbers, "localhost", 8765)

loop = asyncio.get_event_loop()

print("starting server")
loop.run_until_complete(start_server)
loop.run_forever()
