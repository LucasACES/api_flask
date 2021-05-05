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

#! Nome e sobrenome:
nomeall = nomesobrenome('nomeall')
albuN = nomesobrenome('albuquerque')
batiN = nomesobrenome('batista')
carvaN = nomesobrenome('carvalho')
costacomN = nomesobrenome('costacomércio')
costalN = nomesobrenome('costaltda')
melN = nomesobrenome('melo')
pereN = nomesobrenome('pereira')
sanN = nomesobrenome('santos')
souN = nomesobrenome('souza')
xavN = nomesobrenome('xavier')

#! horas:
horasall = horas('horastotal')
albuH = horas('albuquerque')
batiH = horas('batista')
carvaH = horas('carvalho')
costacomH = horas('costacomércio')
costalH = horas('costaltda')
melH = horas('melo')
pereH = horas('pereira')
sanH = horas('santos')
souH = horas('souza')
xavH = horas('xavier')
#?#########################################################################################################################

#! STATUS ROTAS:


@app.route("/data/status/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def status():
    if request.method == "GET":
        return jsonify(statustotal)


@app.route("/data/status/<nome>/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def statusbyprojeto(nome):
    if request.method == "GET":
        if nome == 'albuquerque':
            return jsonify(albu)
        elif nome == 'batista':
            return jsonify(bati)
        elif nome == 'carvalho':
            return jsonify(carva)
        elif nome == 'costacomercio':
            return jsonify(costacom)
        elif nome == 'costaltda':
            return jsonify(costal)
        elif nome == 'melo':
            return jsonify(mel)
        elif nome == 'pereira':
            return jsonify(pere)
        elif nome == 'santos':
            return jsonify(san)
        elif nome == 'souza':
            return jsonify(sou)
        elif nome == 'xavier':
            return jsonify(xav)
        else:
            return "digite um projeto válido"

#?#########################################################################################################################

#! TASKS ROTAS:


@app.route("/data/task/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def task():
    if request.method == "GET":
        return jsonify(statustotalN)


@app.route("/data/task/<nome>/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def taskbyprojeto(nome):
    if request.method == "GET":
        if nome == 'albuquerque':
            return jsonify(albuT)
        elif nome == 'batista':
            return jsonify(batiT)
        elif nome == 'carvalho':
            return jsonify(carvaT)
        elif nome == 'costacomercio':
            return jsonify(costacomT)
        elif nome == 'costaltda':
            return jsonify(costalT)
        elif nome == 'melo':
            return jsonify(melT)
        elif nome == 'pereira':
            return jsonify(pereT)
        elif nome == 'santos':
            return jsonify(sanT)
        elif nome == 'souza':
            return jsonify(souT)
        elif nome == 'xavier':
            return jsonify(xavT)
        else:
            return "digite um projeto válido"

#?#########################################################################################################################

#! NOME ROTAS:


@app.route("/data/nome/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def nome():
    if request.method == "GET":
        return jsonify(nomeall)


@app.route("/data/nome/<nome>/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def nomebyprojeto(nome):
    if request.method == "GET":
        if nome == 'albuquerque':
            return jsonify(albuN)
        elif nome == 'batista':
            return jsonify(batiN)
        elif nome == 'carvalho':
            return jsonify(carvaN)
        elif nome == 'costacomercio':
            return jsonify(costacomN)
        elif nome == 'costaltda':
            return jsonify(costalN)
        elif nome == 'melo':
            return jsonify(melN)
        elif nome == 'pereira':
            return jsonify(pereN)
        elif nome == 'santos':
            return jsonify(sanN)
        elif nome == 'souza':
            return jsonify(souN)
        elif nome == 'xavier':
            return jsonify(xavN)
        else:
            return "digite um projeto válido"

#?#########################################################################################################################

#! NOME ROTAS:


@app.route("/data/horas/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def horas():
    if request.method == "GET":
        return jsonify(horasall)


@app.route("/data/horas/<nome>/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def horasbyprojeto(nome):
    if request.method == "GET":
        if nome == 'albuquerque':
            return jsonify(albuH)
        elif nome == 'batista':
            return jsonify(batiH)
        elif nome == 'carvalho':
            return jsonify(carvaH)
        elif nome == 'costacomercio':
            return jsonify(costacomH)
        elif nome == 'costaltda':
            return jsonify(costalH)
        elif nome == 'melo':
            return jsonify(melH)
        elif nome == 'pereira':
            return jsonify(pereH)
        elif nome == 'santos':
            return jsonify(sanH)
        elif nome == 'souza':
            return jsonify(souH)
        elif nome == 'xavier':
            return jsonify(xavH)
        else:
            return "digite um projeto válido"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
