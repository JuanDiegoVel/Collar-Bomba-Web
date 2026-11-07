"""Servidor local para ver la página del collar bomba con Flask.

Sirve la misma carpeta public/ que se publica en Firebase Hosting.
Uso:  py app.py   y abrir http://127.0.0.1:5000
"""
from pathlib import Path

from flask import Flask, send_from_directory

PUBLIC = Path(__file__).resolve().parent / "public"

app = Flask(__name__, static_folder=None)


@app.get("/")
def inicio():
    return send_from_directory(PUBLIC, "index.html")


@app.get("/<path:ruta>")
def archivos(ruta):
    # send_from_directory no deja salir de public/ con rutas como ../
    return send_from_directory(PUBLIC, ruta)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
