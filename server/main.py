import websockets
import asyncio
from logger import logger
from host.server import Host
PORT = 7890


if __name__ == "__main__":
    server = Host(PORT) 
    async def grupa():
        await asyncio.gather(server.start(),server.read_cli_inputs())
    asyncio.run(grupa())