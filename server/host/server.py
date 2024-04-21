from dataclasses import dataclass, field
import asyncio
import websockets
import json
from routes import RoutesRegistry
from logger import logger
from typing import Any
import aioconsole
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
            
    async def read_cli_inputs(self)->None:
        while True:
            line = await aioconsole.ainput('Is this your line? ')
            match line:
                case "1":
                    await self.clients["ffb24848"].send(message_builder(type="football",data="Gramy w pile"))
                case "2":
                    await self.clients["ffb24848"].send(message_builder(type="outfit",outfit=1,data="nowe ciuszki"))
                    


def message_builder(**kwargs):
    message = json.dumps(kwargs)
    return message