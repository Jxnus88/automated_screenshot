from pynput.mouse import Listener

def region_seleccionada():
    region = []
    
    def on_click(x,y,button,pressed):
        if pressed:
            region.append((x,y))
            print(f"Región seleccionada: ({x}, {y})")
            
            if len(region) == 2:
                return False
            
    print("Selecciona dos puntos opuestos de la región (esquina superior izquierda y luego inferior derecha.)")
    
    with Listener(on_click=on_click) as listener:
        listener.join()
        
    if len(region) != 2:
        raise Exception("Región no seleccionada correctamente.")
    
    x1,y1 = region[0]
    x2,y2 = region[1]
    return (min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2))
