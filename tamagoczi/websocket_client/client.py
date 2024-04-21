import asyncio
import websockets
import json

from routes import RoutesRegistry
from ..tamagoczi.game import Game,Moods

def test_callback(message):
    print(message)

callbacks = {
    "test": test_callback,
    # ... add more as needed
}



async def connect_and_listen():
    url = "ws:///ws" 
    game = Game("12345","Szymon Walczak",0,Moods.DEFAULT,"",100)
    async with websockets.connect(url) as websocket:


        while True:
            response = await websocket.recv()

            try:
                message = json.loads(response)  
                print(message)
                message_type = message.get("type") 

                if message_type in RoutesRegistry.handlers:
                    callbacks[message_type](websocket,message)
                else:
                    print(f"Unknown message type: {message_type}")

            except json.JSONDecodeError:
                print("Invalid JSON data received.")
            except Exception as e:
                print(f"Error processing message: {e}")

asyncio.run(connect_and_listen())