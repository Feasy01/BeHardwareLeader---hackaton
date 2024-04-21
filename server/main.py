import websockets
import asyncio
from logger import logger
from host.server import Host
PORT = 7890


if __name__ == "__main__":
    server = Host(PORT) 
    asyncio.run(server.start())