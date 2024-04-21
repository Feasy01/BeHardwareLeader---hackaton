import asyncio
import websockets
import json



def test_callback(message):
    print(message)

callbacks = {
    "test": test_callback,
    # ... add more as needed
}



async def connect_and_listen():
    url = "wss://example.com/ws"  # Replace with your WebSocket server URL
    async with websockets.connect(url) as websocket:


        while True:
            response = await websocket.recv()

            try:
                message = json.loads(response)  
                print(message)
                message_type = message.get("type") 

                if message_type in callbacks:
                    callbacks[message_type](message.get("data"))
                else:
                    print(f"Unknown message type: {message_type}")

            except json.JSONDecodeError:
                print("Invalid JSON data received.")
            except Exception as e:
                print(f"Error processing message: {e}")

asyncio.run(connect_and_listen())