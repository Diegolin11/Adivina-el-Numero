# Adivina el Número — Proyecto Web con Flask

Juego web simple donde el usuario intenta adivinar un número entre 1 y 100.
Este proyecto usa Flask para el backend y HTML/CSS para la interfaz.

## Contenido
- `juego.py` — lógica del servidor 
- `templates/index.html` — plantilla HTML
- `static/styles.css` — estilos
- `requirements.txt` — dependencias
- `LICENSE` — licencia MIT

## Requisitos
- Python 3.8+ recomendado
- pip

## Instalación (paso a paso)

1. Clonar o copiar el proyecto a una carpeta, por ejemplo `adivina_numero`.

2. Abrir terminal y crear entorno virtual:
   ```bash
   python3 -m venv venv

   activar el entorno virtual con: venv\Scripts\activate
   el prompt tiene que cambiar en su inicio a (venv)

3. Instalar las dependencias:
   ```bash
   pip install -r requerimientos.txt ESTO depende el nombre que tenga el archivo txt

   si no instala nada puedes instalar flask directamente con: pip install flask (desde la terminal)

4. Ejecutar el juego
    ```bash
    en la terminal usamos python juego.py
    despues aparecera una liga como algo asi  http://127.0.0.1:5000 

    La copiamos y en nuestro navegador debera aparecer nuestro juego 

5. Detener el juego
   ```bash
   regresas a la terminal y presionamos crtl + c