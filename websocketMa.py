import json

class WebSocketManager:
    def __init__(self):
        self.active_connectors = []
        
        #fct pour se connecter
    async def connect(self, websocket):
        await websocket.accept()
        self.active_connectors.append(websocket)
            
        #fct pour se deconnecter
    def disconnect(self, websocket):
        if websocket in self.active_connectors:
            self.active_connnectors.remove(websocket)
                
        #fct pour envoyer un meaage de diffusion
    async def broadcast(self, message: dict):
        data = json.dumps(message)
        for connector in self.active_connectors:
            try:
                await connector.send_text(data)
            except Exception:
                self.disconnect(connector)