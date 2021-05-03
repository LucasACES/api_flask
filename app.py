from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
import os
from model.funcoes import *


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/data/status/*": {"origins": "*"}})
#! STATUS:
statustotal = status('statusall')
albu = status('albuquerque')
bati = status('batista')
carva = status('carvalho')
costacom = status('costacomércio')
costal = status('costaltda')
mel = status('melo')
pere = status('pereira')
san = status('santos')
sou = status('souza')
xav = status('xavier')

#! TASKS:
statustotalT = task('statusall')
albuT = task('albuquerque')
batiT = task('batista')
carvaT = task('carvalho')
costacomT = task('costacomércio')
costalT = task('costaltda')
melT = task('melo')
pereT = task('pereira')
sanT = task('santos')
souT = task('souza')
xavT = task('xavier')

#! STATUS ROTAS:


@app.route("/data/status/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def trello():
    if request.method == "GET":
        return jsonify(statustotal)


@app.route("/data/status/albuquerque/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def albuquerque():
    if request.method == "GET":
        return jsonify(albu)


@app.route("/data/status/batista/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def batista():
    if request.method == "GET":
        return jsonify(bati)


@app.route("/data/status/carvalho/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def carvalho():
    if request.method == "GET":
        return jsonify(carva)


@app.route("/data/status/costacomercio/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def costacomercio():
    if request.method == "GET":
        return jsonify(costacom)


@app.route("/data/status/costaltda/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def costaltda():
    if request.method == "GET":
        return jsonify(costal)


@app.route("/data/status/melo/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def melo():
    if request.method == "GET":
        return jsonify(mel)


@app.route("/data/status/pereira/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def pereira():
    if request.method == "GET":
        pereira = pereira()
        return jsonify(pere)


@app.route("/data/status/santos/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def santos():
    if request.method == "GET":
        return jsonify(san)


@app.route("/data/status/souza/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def souza():
    if request.method == "GET":
        return jsonify(sou)


@app.route("/data/status/xavier/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def xavier():
    if request.method == "GET":
        return jsonify(xav)

#?#########################################################################################################################

#! TASKS ROTAS:


@app.route("/data/task/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def task():
    if request.method == "GET":
        return jsonify(statustotalT)


@app.route("/data/task/albuquerque/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def albuquerqueT():
    if request.method == "GET":
        return jsonify(albuT)


@app.route("/data/task/batista/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def batistaT():
    if request.method == "GET":
        return jsonify(batiT)


@app.route("/data/task/carvalho/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def carvalhoT():
    if request.method == "GET":
        return jsonify(carvaT)


@app.route("/data/task/costacomercio/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def costacomercioT():
    if request.method == "GET":
        return jsonify(costacomT)


@app.route("/data/task/costaltda/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def costaltdaT():
    if request.method == "GET":
        return jsonify(costalT)


@app.route("/data/task/melo/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def meloT():
    if request.method == "GET":
        return jsonify(melT)


@app.route("/data/task/pereira/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def pereiraT():
    if request.method == "GET":
        pereira = pereira()
        return jsonify(pereT)


@app.route("/data/task/santos/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def santosT():
    if request.method == "GET":
        return jsonify(sanT)


@app.route("/data/task/souza/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def souzaT():
    if request.method == "GET":
        return jsonify(sou)


@app.route("/data/task/xavier/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def xavierT():
    if request.method == "GET":
        return jsonify(xavT)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
