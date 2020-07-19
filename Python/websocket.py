import socket
from time import sleep
import websockets
import asyncio


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
        async for message in websocket:
            x = message
            print(x)
        

start_server = websockets.serve(echo, "localhost", 8123)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
