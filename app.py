import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/dados/*": {"origins": "*"}})

data_json_file = open(file='dadosFormatados.json')
data_all = json.load(data_json_file)
data_json_file.close()

status_count_json_file = open(file='status_count.json')
status_count = json.load(status_count_json_file)
status_count_json_file.close()


@app.route("/dados/data/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def data():
    if request.method == "GET":
        return jsonify(data_all)


@app.route("/dados/status", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def trello():
    if request.method == "GET":
        return jsonify(status_count)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
