from f_coordenadas import obtener_coordenada
from f_screen import region_seleccionada
from f_click import repetir_click_y_screenshot
from pynput.keyboard import Listener
import time

program_running = True

def on_press(key):
    global program_running
    try:
        if key.char == 'q':
            print("Tecla 'q' presionada. Deteniendo el programa...")
            program_running = False
            return False
    except AttributeError:
        pass

# Iniciar listener de teclado
listener = Listener(on_press=on_press)
listener.start()

# Paso 1: Coordenada de clic
posicion_click = obtener_coordenada()
print(f"Posición seleccionada: {posicion_click}")

# Paso 2: Región de screenshot
region = region_seleccionada()
print(f"Región seleccionada: {region}")

# Paso 3: Cantidad
while True:
    try:
        cantidad = int(input("¿Cuántas veces deseas repetir el clic?: "))
        if cantidad > 0:
            break
        else:
            print("Debe ser un número mayor que 0.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Paso 4: Ejecutar
delay = 10  # segundos entre clics
repetir_click_y_screenshot(
    pos=posicion_click,
    region=region,
    n=cantidad,
    delay=delay,
    stop_flag_fn=lambda: not program_running
)
