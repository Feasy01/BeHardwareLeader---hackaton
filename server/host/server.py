from dataclasses import dataclass, field
import asyncio
import websockets
import json
from routes import RoutesRegistry
from logger import logger
from typing import Any

from game.game import Game

@dataclass
class Host:
    port:int
    clients:dict[str:Any] = field(default_factory=lambda: {})
    def __post_init__(self):
        self.game = Game()
    async def handler(self,websocket) -> None:
        
        while True:
            message = await websocket.recv()
            logger.info(message)
            try:
                parsed_message = json.loads(message)               
                type = parsed_message.get("type")
                callback_function = RoutesRegistry.handlers[type]
                await callback_function(self,parsed_message,websocket,self.game)
            except Exception as e:
                logger.error(f"{e}")
                raise RuntimeError("lipa")
    async def start(self)->None:
        async with websockets.serve(self.handler, "", self.port,ping_interval=20, ping_timeout=10):
            logger.info(f"server started on port {self.port}")
            await asyncio.Future()  
        