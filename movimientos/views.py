from movimientos import app
from flask import render_template
import csv

@app.route('/')
def listaingresos():
    fIngresos = open("movimientos/data/basededatos.csv", "r")
    csvReader = csv.reader(fIngresos, delimiter=',', quotechar="\"")
    ingresos = list(csvReader)

    total = 0
    for ingreso in ingresos:
        total += float(ingreso[2])


    return render_template("movimientoslista.html",datos=ingresos, total=total)

@app.route('/creaalta')
def nuevoIngreso():
    return 'Ya el miércoles si eso te enseño el formulario'


