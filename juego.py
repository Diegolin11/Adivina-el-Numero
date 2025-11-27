
# Flask: Framework ligero para crear aplicaciones web con Python.
# - Flask: Permite crear la aplicación web.
# - render_template: Permite mostrar archivos HTML.
# - request: Permite recibir datos enviados desde formularios HTML.
# - session: Guarda datos temporales del usuario (como el número secreto).
# - redirect: Permite redirigir al usuario hacia otra ruta/URL dentro del sitio.
from flask import Flask, render_template, request, session, redirect

# random: Librería estándar de Python para generar números aleatorios,
# en este caso el número secreto que el usuario debe adivinar.
import random


# ============================================================
#  Configuración inicial de la aplicación Flask
# ============================================================

# Se crea una instancia de la aplicación Flask.
app = Flask(__name__)

# Clave secreta necesaria para manejar las sesiones.
# Sin esta clave, Flask no puede guardar variables en "session".
app.secret_key = "clave-super-secreta"


# ============================================================
#  Ruta para reiniciar el juego
# ============================================================

@app.route("/reset")
def reset():
    """
    Esta función reinicia el juego eliminando los valores guardados en la sesión.
    Borra el número secreto y el contador de intentos.
    Después redirige al usuario nuevamente a la página principal.
    """

    # Eliminamos las variables de sesión si existen
    session.pop("numero_secreto", None)
    session.pop("intentos", None)

    # Redirigimos al usuario al inicio
    return redirect("/")


# ============================================================
#  Página principal del juego (logica + interfaz)
# ============================================================

# La ruta "/" acepta métodos GET y POST:
# - GET  → mostrar la página
# - POST → recibir un intento del usuario
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Vista principal del juego.
    Contiene TODA la lógica del programa:
    - Genera el número secreto (si no existe)
    - Recibe el intento del usuario
    - Decide si es mayor, menor o correcto
    - Lleva el conteo de intentos
    """

    # ------------------------------------------------------------
    # 1. Generar número secreto (si aún no está en la sesión)
    # ------------------------------------------------------------

    if "numero_secreto" not in session:
        # Numero entre 1 y 100
        session["numero_secreto"] = random.randint(1, 100)
        session["intentos"] = 0  # contador de intentos


    mensaje = ""  # Mensaje que se mostrará al usuario


    # ------------------------------------------------------------
    # 2. Si el usuario envió un número (POST)
    # ------------------------------------------------------------

    if request.method == "POST":
        try:
            # Convertimos el valor recibido desde el formulario a entero
            intento = int(request.form["numero"])
        except ValueError:
            # Si el usuario envía texto o algo no válido
            mensaje = "⚠️ Ingresa un número válido."
            return render_template("index.html", mensaje=mensaje, intentos=session["intentos"])

        # Aumentamos el número de intentos
        session["intentos"] += 1

        # Recuperamos el número secreto almacenado
        secreto = session["numero_secreto"]


        # ------------------------------------------------------------
        # 3. Comparación del intento vs el número secreto
        # ------------------------------------------------------------

        if intento < secreto:
            mensaje = "➡️ Muy bajo"
        elif intento > secreto:
            mensaje = "⬆️ Muy alto"
        else:
            # ¡Acertó!
            mensaje = f"🎉 ¡Correcto! Lo lograste en {session['intentos']} intentos."

            # Reiniciamos el juego borrando los valores de sesión
            session.pop("numero_secreto")
            session.pop("intentos")


    # ------------------------------------------------------------
    # 4. Renderizamos la plantilla HTML
    # ------------------------------------------------------------

    return render_template(
        "index.html",
        mensaje=mensaje,
        intentos=session.get("intentos", 0)
    )


# ============================================================
#  Ejecutar el servidor Flask
# ============================================================

if __name__ == "__main__":
    # debug=True reinicia la app automáticamente si cambias el código.
    app.run(debug=True)
