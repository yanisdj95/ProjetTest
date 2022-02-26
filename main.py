from flask import request
import flask
import pymysql
from flask import jsonify

def connection():
    db = pymysql.connect(database='testprojet', host='localhost', user='root', password='')
    print("Connexion réussie")
    return db

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/all', methods=['GET'])
def get_all():
    sql_0 = "SELECT * FROM `chaussure`;"
    db = connection()
    cursor = db.cursor()
    cursor.execute(sql_0)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/<id>', methods=['GET'])
def get_one(id):
    sql_1 = "SELECT * FROM `chaussure` WHERE id = " + id + ";"
    db = connection()
    cursor = db.cursor()
    cursor.execute(sql_1)
    result = cursor.fetchone()
    return jsonify(result)

@app.route('/delete/<id>', methods=['DELETE'])
def delete_one(id):
    sql_delete = "DELETE FROM `chaussure` WHERE id = " + id + ";"
    db = connection()
    cursor = db.cursor()
    cursor.execute(sql_delete)
    return jsonify({"deleted_succes" : id})

@app.route('/post', methods=['POST'])
def post_one():
    db = connection()
    id = request.json['id']
    marque = request.json['marque']
    modele = request.json['modele']
    prix = request.json['prix']
    sql_2 = "INSERT INTO `chaussure` (marque, modele, prix) VALUES ('" +marque+"','"+modele+"'," + str(prix) + ");"
    cursor = db.cursor()
    cursor.execute(sql_2)
    return jsonify({"id" : id, "marque" : marque, "modele" : modele, "prix" : prix})

app.run()
