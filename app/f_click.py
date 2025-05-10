import os
from datetime import datetime
from pynput.mouse import Controller, Button
from PIL import ImageGrab
import time

mouse = Controller()

def repetir_click_y_screenshot(pos, region, n, delay=0.1, stop_flag_fn=lambda: False):
    # Crear carpeta con timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"screenshots_{timestamp}"
    os.makedirs(folder_name, exist_ok=True)

    print(f"Iniciando {n} clics en {pos} con capturas en la región {region}...")
    print(f"Las imágenes se guardarán en: {folder_name}/")

    # Cuenta regresiva
    for i in range(3, 0, -1):
        print(f"Comenzando en {i}...")
        time.sleep(1)

    for i in range(n):
        if stop_flag_fn():
            print("Proceso detenido por el usuario.")
            break

        current_pos = mouse.position
        mouse.position = pos
        mouse.click(Button.left, 1)
        mouse.position = current_pos
        time.sleep(delay)

        screenshot = ImageGrab.grab(bbox=region)
        image_path = os.path.join(folder_name, f"screenshot_{i+1}.png")
        screenshot.save(image_path)
        print(f"Captura {i+1} guardada: {image_path}")

    print("Proceso terminado.")
