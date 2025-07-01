from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask (__name__)


os.makedirs("logs", exist_ok=True)

def guardar_log(operacion, resultado):
    with open("logs/log.txt", "a") as archivo:
        archivo.write(f"{datetime.now()} - {operacion} = {resultado}\n")

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            numero1 = float(request.form["numero1"])
            numero2 = float(request.form["numero2"])
            operacion = request.form["operacion"].lower().strip()

            if operacion == "suma":
                resultado = numero1 + numero2
            elif operacion == "resta":
                resultado = numero1 - numero2
            elif operacion == "multiplicacion":
                resultado = numero1 * numero2
            elif operacion == "division":
                if numero2 == 0:
                    error = "Error no se puede dividir entre cero."
                else:
                    resultado = numero1 / numero2
            else:
                error = "Operación no válida. "

            if resultado is not None:
               guardar_log(f"{numero1} {operacion} {numero2}", resultado)

        except ValueError:
            error = "Por favor ingrese números válidos."

    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

