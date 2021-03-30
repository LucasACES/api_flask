import json
import os
from flask import Flask, jsonify, request
from flask-cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/dados/*": {"origins": "*"}})

jira_json_file = open(file='jira_formatted.json')
trello_json_file = open(file='trello_formatted.json')

jira_data = json.load(jira_json_file)
trello_data = json.load(trello_json_file)

jira_json_file.close()
trello_json_file.close()


@app.route("/dados/jira/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def jira():
    if request.method == "GET":
        return jsonify(jira_data)


@app.route("/dados/trello/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def trello():
    if request.method == "GET":
        return jsonify(trello_data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
