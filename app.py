import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify
import json
from flask import jsonify
import pandas as pd



from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:Youtube111!!!@localhost:5432/OAB_database')
connection = engine.connect()

df = pd.read_sql_query('SELECT * FROM public."OAB"',con=engine)
AB_C = pd.read_sql_query('SELECT * FROM public."AB_C"',con=engine)
ON_C = pd.read_sql_query('SELECT * FROM public."ON_C"',con=engine)
ON_F_C = pd.read_sql_query('SELECT * FROM public."ON_F_C"',con=engine)
AB_F_C = pd.read_sql_query('SELECT * FROM public."AB_F_C"',con=engine)


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def html_table():
    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/data', methods=["GET"])
def send_data():
    json_file = df.to_json(orient='records')
    j_l = json.loads(json_file)
    return jsonify(j_l)

@app.route('/data/ab_c', methods=["GET", "POST"])
def x_data():
    json_file = AB_C.to_json(orient='records')
    x_l = json.loads(json_file)
    return jsonify(x_l)

@app.route('/data/on_c', methods=["GET"])
def y_data():
    json_file = ON_C.to_json(orient='records')
    x_l = json.loads(json_file)
    return jsonify(x_l)

@app.route('/data/on_f_c', methods=["GET"])
def z_data():
    json_file = ON_F_C.to_json(orient='records')
    x_l = json.loads(json_file)
    return jsonify(x_l)

@app.route('/data/ab_f_c', methods=["GET"])
def w_data():
    json_file = AB_F_C.to_json(orient='records')
    x_l = json.loads(json_file)
    return jsonify(x_l)


if __name__ == "__main__":
    app.run(debug=True)
