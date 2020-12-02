from movimientos import app
from flask import render_template

@app.route('/')
def listaMovimientos():
    return render_template("movimientoslista.html", miTexto="Aquí pongo lo que quiero directamente como una función")