from typing import Callable
import websockets
import json
from game.game import Game
from logger import logger


class RoutesRegistry:
    handlers = {}

    @classmethod
    def reg_route(cls, route_handler: Callable):
        if route_handler is not None:
            cls.handlers[route_handler.__name__] = route_handler
        else:
            raise RuntimeError("giga problem posiadamy")


@RoutesRegistry.reg_route
async def test(server, message, websocket, game):
    await websocket.send("test")


@RoutesRegistry.reg_route
async def error(server, message, websocket, game):
    await websocket.send("error")


@RoutesRegistry.reg_route
async def access(server, message, websocket, game: Game):
    try:
        rf_id = message.get("data")
        user_websocket = server.clients[rf_id]
        user_game = game.users.get(rf_id)
        response = message_builder(
            localization=message.get("localization"), type="access",points=user_game.go_somewhere_points
        )
        await user_websocket.send(response)
        user_game.go_somewhere_points = 0
    except KeyError:
        await websocket.send("Nie ma usera powiazanego z tym tagiem")


@RoutesRegistry.reg_route
async def init(server, message, websocket, game: Game):
    try:
        rf_id = message.get("rf_id")
        name = message.get("name")
        points = message.get("points")
        outfit = message.get("outfit")

        server.clients[rf_id] = websocket
        if rf_id not in game.users.keys():
            game.add_user(rf_id, name, points, outfit)
    except Exception as e:
        logger.error(f"{e}")
        
@RoutesRegistry.reg_route
async def action(server,message,websocket,game:Game):
    rf_id = message.get("rf_id")
    action_message = message.get("data")
    points_value = message.get("points")
    user_game = game.users.get(rf_id)
    user_game.go_somewhere_points += points_value
    user_websocket = server.clients[rf_id]
    
    response = message_builder(action_message=action_message,type="action",points_value=points_value)
    await user_websocket.send()

@RoutesRegistry.reg_route
async def get_users(server,message,websocket,game):
    users = game.users.values()
    dump = list(users)
    response = message_builder(data=dump, type="get_users")
    await websocket.send(response)


def message_builder(**kwargs):
    message = json.dumps(kwargs)
    return message
