import uvicorn
import asyncio
from fastapi import FastAPI, WebSocket
from websocketMa import WebSocketManager
from manager import start_data_generator
from control import handle_message

ws_manager = WebSocketManager()

async def lifespan(app: FastAPI):
    asyncio.create_task(start_data_generator(ws_manager))
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Hello DRMN"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await handle_message(data, ws_manager)
    except Exception:
        ws_manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
