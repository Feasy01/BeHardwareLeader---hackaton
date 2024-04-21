from typing import Callable
import websockets
class RoutesRegistry:
    handlers = {}
    
    @classmethod
    def reg_route(cls,route_handler:Callable):
        if route_handler is not None:
            cls.handlers[route_handler.__name__] = route_handler
        else:
            raise RuntimeError("giga problem posiadamy")
        

@RoutesRegistry.reg_route
def test(websocket):
    websocket.send("test")

@RoutesRegistry.reg_route
def error(websocket):
    websocket.send("error")