from typing import Callable
import websockets
from ..tamagoczi.game import Moods, Game
class RoutesRegistry:
    handlers = {}
    
    @classmethod
    def reg_route(cls,route_handler:Callable):
        if route_handler is not None:
            cls.handlers[route_handler.__name__] = route_handler
        else:
            raise RuntimeError("giga problem posiadamy")


@RoutesRegistry.reg_route
async def football(websocket,message,game:Game):
    await game.change_mood(Moods.FOOTBALL)
    await game.change_action(message.get("data"))
    
@RoutesRegistry.reg_route
async def outfit(websockets,message,game:Game):
    await game.change_outfit(message.get("outfit"))
    await game.change_action(message.get("data"))


@RoutesRegistry.reg_route
async def error(websocket,message,game:Game):
    websocket.send("error")