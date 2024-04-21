import asyncio
import websockets
import json

from .routes import RoutesRegistry
from ..tamagoczi.game import Game,Moods


async def connect_and_listen(oled_hook, lcd_hook):
    url = "ws://192.168.137.220:7890/ws" 
    game = Game("ffb24848","Szymon Walczak",0,Moods.DEFAULT,"",100,oled_hook, lcd_hook)
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps({"type":"init","rf_id":"ffb24848", "name":"Szymon Walczak", 
                                   "points":100, "outfit":0}))
        print("Connected to server.")

        while True:
            response = await websocket.recv()

            try:
                message = json.loads(response)  
                print(message)
                message_type = message.get("type") 

                if message_type in RoutesRegistry.handlers:
                    await RoutesRegistry.handlers[message_type](websocket,message,game)
                else:
                    print(f"Unknown message type: {message_type}")

            except json.JSONDecodeError:
                print("Invalid JSON data received.")
            except Exception as e:
                print(f"Error processing message: {e}")

# asyncio.run(connect_and_listen())