import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


def openfile(arq):
    json_file = open(file=f'{arq}')
    arquivoo = json.load(json_file)
    json_file.close()
    return arquivoo


cors = CORS(app, resources={r"/data/*": {"origins": "*"}})

status_all = openfile('status_count.json')
Albuquerque = openfile(
    './projetosStatus/status_count_[Albuquerque, Albuquerque and Carvalho Comércio] - Mandatory human-resource open architecture.json')
Batista = openfile(
    './projetosStatus/status_count_[Batista, Moreira and Pereira LTDA] - Monitored multi-state installation.json')
Carvalho = openfile(
    './projetosStatus/status_count_[Carvalho, Costa and Costa e Associados] - Ergonomic methodical methodology.json')
Costa_Comércio = openfile(
    './projetosStatus/status_count_[Costa Comércio Comércio] - Sharable non-volatile internet solution.json')
Costa_LTDA = openfile(
    './projetosStatus/status_count_[Costa LTDA S.A.] - Total asynchronous secured line.json')
Melo = openfile(
    './projetosStatus/status_count_[Melo, Melo and Santos e Associados] - Organized impactful instruction set.json')
Pereira = openfile(
    './projetosStatus/status_count_[Pereira - Barros Comércio] - Mandatory fault-tolerant Graphical User Interface.json')
Santos = openfile(
    './projetosStatus/status_count_[Santos - Batista Comércio] - Stand-alone well-modulated policy.json')
Souza = openfile(
    './projetosStatus/status_count_[Souza Comércio e Associados] - Innovative background implementation.json')
Xavier = openfile(
    './projetosStatus/status_count_[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')


@app.route("/data/status/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def trello():
    if request.method == "GET":
        return jsonify(status_all)


@app.route("/data/albuquerque/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def albuquerque():
    if request.method == "GET":
        return jsonify(Albuquerque)


@app.route("/data/batista/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def batista():
    if request.method == "GET":
        return jsonify(Batista)


@app.route("/data/carvalho/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def carvalho():
    if request.method == "GET":
        return jsonify(Carvalho)


@app.route("/data/costacomercio/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def costacomercio():
    if request.method == "GET":
        return jsonify(Costa_Comércio)


@app.route("/data/costaltda/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def costaltda():
    if request.method == "GET":
        return jsonify(Costa_LTDA)


@app.route("/data/melo/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def melo():
    if request.method == "GET":
        return jsonify(Melo)


@app.route("/data/pereira/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def pereira():
    if request.method == "GET":
        return jsonify(Pereira)


@app.route("/data/santos/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def santos():
    if request.method == "GET":
        return jsonify(Santos)


@app.route("/data/souza/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def souza():
    if request.method == "GET":
        return jsonify(Souza)


@app.route("/data/xavier/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def xavier():
    if request.method == "GET":
        return jsonify(Xavier)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
