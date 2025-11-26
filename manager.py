import asyncio
import random 
from log_contol import LogControl

#une seconde entre 2 data
frequency = 1 
#la valeur seuil
threshold = 50
#etat du systeme
running = True 

log_control = LogControl()

async def start_data_generator(ws_manager):
    global running
    asyncio.create_task(generator_loop(ws_manager))

async def generator_loop(ws_manager):
    global running, frequency, threshold
    while True:
        if running:
            value = random.randint(0, 100)
            message = {"type": "data", "value": value}

            # Vérification du seuil
            if value > threshold:
                alert = f"ALERTE: valeur {value} > seuil {threshold}"
                log_control.add_log(alert)
                message["alert"] = alert

            await ws_manager.broadcast(message)

        await asyncio.sleep(frequency)