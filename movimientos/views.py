from movimientos import app
from flask import render_template, request, url_for, redirect
import csv
import sqlite3


@app.route('/')
def listaIngresos():
    conn = sqlite3.connect('movimientos/data/basededatos.db')
    c = conn.cursor()

    c.execute('SELECT fecha, concepto, cantidad, id FROM movimientos;')

    ingresos = c.fetchall()

    total = 0
    for ingreso in ingresos:
        total += float(ingreso[2])

    conn.close()

    return render_template("movimientoslista.html",datos=ingresos, total=total)

@app.route('/creaalta', methods=['GET', 'POST'])
def nuevoIngreso():
    if request.method == 'POST':

        conn = sqlite3.connect('movimientos/data/basededatos.db')
        c = conn.cursor()

        c.execute('INSERT INTO movimientos (cantidad, concepto, fecha) VALUES (?, ? ,? );', 
                 (
                    float(request.form.get('cantidad')),
                    request.form.get('concepto'),
                    request.form.get('fecha')
                 )
        )

        conn.commit()
        conn.close()
    
        return redirect(url_for('listaIngresos'))
        


    return render_template("alta.html")

@app.route("/modifica/<id>", methods=['GET', 'POST'])
def modifica(id):
    conn = sqlite3.connect('movimientos/data/basededatos.db')
    c = conn.cursor()

    if request.method == 'GET':
        
        c.execute('SELECT fecha, concepto, cantidad id FROM movimientos where id = ?', (id,))
        registro = c.fetchone()
        conn.close()

        return render_template("modifica.html", registro=registro)


    else:
        c.execute('UPDATE movimientos SET fecha = ?, concepto = ?, cantidad = ? WHERE id = ?',
            (request.form.get('fecha'),
            request.form.get('concepto'),
            float(request.form.get('cantidad')),
            id
            )
        )
        conn.commit()
        conn.close()

        return redirect(url_for('listaIngresos'))
    









