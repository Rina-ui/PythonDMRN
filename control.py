import json
from manager import frequency, threshold, running

async def handle_message(data, ws_manager):
    global frequency, threshold, running
    message = json.loads(data)

    if message["action"] == "SET_FREQUENCY":
        frequency = float(message["value"])
    elif message["action"] == "SET_THRESHOLD":
        threshold = int(message["value"])
    elif message["action"] == "STOP":
        running = False
    elif message["action"] == "START":
        running = True

    # Confirmation send au client
    await ws_manager.broadcast({"type": "control", "status": message})
