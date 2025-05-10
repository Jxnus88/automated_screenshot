from pynput.mouse import Listener

def obtener_coordenada():
    coordenadas = []
    
    def on_click(x,y,button,pressed):
        if pressed:
            coordenadas.append((x,y))
            return False
        
    with Listener(on_click=on_click) as listener:
        listener.join()
        
    return coordenadas[0] if coordenadas else None