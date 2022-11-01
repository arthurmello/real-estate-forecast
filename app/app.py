from distutils.log import debug
from estimation import preprocessing, estimate
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
list_cp = [
    31100, 31300,31400, 31270, 31600,31170,31700,31120,
    31820,31100,31470,31500,31200
    ]
list_local = ["Appartement", "Maison"]

@app.route('/')
def my_form():
    return render_template('index.html', list_cp=list_cp, list_local=list_local)

@app.route('/', methods=['GET', 'POST'])
def estimate_price():
    surface_reelle_bati = float(request.form['surface_reelle_bati'])
    surface_terrain = float(request.form['surface_terrain'])
    code_postal = int(request.form['code_postal'])
    nombre_pieces_principales = int(request.form['nombre_pieces_principales'])
    type_local = request.form['type_local']
    prixcible = float(request.form['prixcible'])
    df = pd.DataFrame.from_dict({
        'surface_reelle_bati':[surface_reelle_bati],
        'surface_terrain':[surface_terrain],
        'code_postal': [code_postal],
        'nombre_pieces_principales':[nombre_pieces_principales],
        'type_local':[type_local],
        'prixcible':[prixcible]
        })
    df = preprocessing(df)
    result = estimate(df)
    return render_template("index.html", result = result, code_postal = code_postal, list_cp=list_cp, list_local=list_local, type_local=type_local)

if __name__ == '__main__':
   app.run(debug=True)