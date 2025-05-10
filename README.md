# Automated Screenshot & Clicker

Este proyecto es una herramienta para automatizar clics del ratón y tomar capturas de pantalla en una región seleccionada. El programa permite seleccionar una ubicación para los clics y una región de pantalla para capturar. Además, las capturas se guardan en una carpeta con nombre único basado en la fecha y hora de la ejecución.

## Características

- Selección de la posición donde realizar los clics.
- Selección de la región para las capturas de pantalla.
- Es posible repetir los clics y capturas el número de veces que el usuario desee.
- Detención del proceso en cualquier momento presionando la tecla q.
- Las imágenes capturadas se guardan automáticamente en una carpeta específica con nombre único basado en la fecha y hora de ejecución.

## Requisitos

Para ejecutar este proyecto necesitas tener instaladas las siguientes bibliotecas:

- `pynput`: Para controlar el ratón y escuchar las teclas del teclado.
- `Pillow`: Para capturar las pantallas.

## Instalación

1. Clona o descarga este repositorio.
2. Abre una terminal y navega hasta la carpeta donde se descargó el proyecto.
3. Instala las dependencias necesarias:
    ```bash
    pip install pynput Pillow
    ```

## Instrucciones de Uso

### Ejecutar el Script

1. Abre una terminal en el directorio donde se encuentran los scripts y ejecuta el script principal:
    ```bash
    python main.py
    ```

### Paso a paso:

1. **Selecciona la posición donde hacer clic:**
    El programa te pedirá que hagas un clic en la ubicación donde quieres que se repitan los clics. Haz clic en cualquier lugar de tu pantalla y la posición será capturada.

2. **Selecciona la región para las capturas de pantalla:**
    A continuación, el programa te pedirá que selecciones dos puntos en la pantalla (esquina superior izquierda e inferior derecha) para definir la región que se va a capturar.

3. **Introduce la cantidad de clics:**
    Luego, se te pedirá que indiques cuántas veces deseas repetir el clic y la captura de pantalla.

4. **Detén el programa en cualquier momento:**
    Si presionas la tecla 'q', el programa se detendrá inmediatamente.

### Resultado:

Las capturas de pantalla se guardarán automáticamente en una carpeta cuyo nombre será algo como `screenshots_2025-05-10_19-02-31`, dentro de la cual se guardarán las imágenes como `screenshot_1.png`, `screenshot_2.png`, etc.

### Ejemplo de Uso

1. **Prepara el entorno:**  
    Asegúrate de tener `pynput` y `Pillow` instalados, como se explicó anteriormente.

2. **Ejecutar el script:**  
    Navega hasta el directorio donde se encuentra `main.py` y ejecuta el siguiente comando en la terminal:
    ```bash
    python main.py
    ```

3. **Selecciona la posición para los clics:**  
    El programa te pedirá que selecciones el lugar donde se realizarán los clics. Haz clic en cualquier parte de tu pantalla.  
    Ejemplo:  
    ```bash
    Posición del clic seleccionada: (123, 456)
    ```

4. **Selecciona la región para el screenshot:**  
    Luego, el programa te pedirá que selecciones dos puntos de la pantalla para definir la región de la captura. Haz clic en la esquina superior izquierda de la región, y luego en la esquina inferior derecha.  
    Ejemplo:  
    ```bash
    Región seleccionada: (100, 200, 800, 600)
    ```

5. **Introduce la cantidad de clics:**  
    El programa te preguntará cuántas veces quieres repetir el clic y la captura. Ingresa un número positivo:  
    Ejemplo:  
    ```bash
    ¿Cuántas veces deseas repetir el clic?: 5
    ```

6. **Proceso en marcha:**  
    Después de una cuenta regresiva, el script comenzará a hacer clics y capturas de pantalla. Durante el proceso, las imágenes se guardarán en una carpeta con la fecha y hora actual:  
    Ejemplo:  
    ```bash
    Las imágenes se guardarán en: screenshots_2025-05-10_19-02-31/
    ```

7. **Ejemplo de salida:**  
    ```bash
    Posición del clic seleccionada: (123, 456)
    Región seleccionada: (100, 200, 800, 600)
    ¿Cuántas veces deseas repetir el clic?: 5
    El programa comenzará en 3 segundos...
    Comenzando en 3...
    Comenzando en 2...
    Comenzando en 1...
    Iniciando 5 clics en (123, 456) con capturas en la región (100, 200, 800, 600)...
    Captura 1 guardada: screenshots_2025-05-10_19-02-31/screenshot_1.png
    Captura 2 guardada: screenshots_2025-05-10_19-02-31/screenshot_2.png
    Captura 3 guardada: screenshots_2025-05-10_19-02-31/screenshot_3.png
    Captura 4 guardada: screenshots_2025-05-10_19-02-31/screenshot_4.png
    Captura 5 guardada: screenshots_2025-05-10_19-02-31/screenshot_5.png
    Proceso terminado.
    ```

8. **Detener el proceso:**  
    Puedes presionar la tecla 'q' en cualquier momento para detener el proceso:  
    ```bash
    Tecla 'q' presionada. Deteniendo el programa...
    ```

[![Ver el video]((https://www.youtube.com/watch?v=BxwY-d_WXlU))


## Contribución

Si deseas contribuir al proyecto, puedes hacer un fork y enviar pull requests con mejoras o correcciones. ¡Estaré encantado de revisarlos!

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
