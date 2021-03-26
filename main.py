import json
import os

from psycopg2 import connect
from psycopg2.extras import Json
from flask import Flask, jsonify, request

app = Flask(__name__)


jira_json_file = open(file='jira_formatted.json')
trello_json_file = open(file='trello_formatted.json')

# Lendo o arquivo como Json.
jira_data = json.load(jira_json_file)
trello_data = json.load(trello_json_file)

# Fechando o arquivo, visto que ele não é mais necessário.
jira_json_file.close()
trello_json_file.close()


@app.route('/jira/')
def jira():
    if request.headers.get('a') == 'Acess-Control-Allow-Origin':
        return jsonify(jira_data), 200
    return jsonify(jira_data), 200


@app.route('/trello/')
def trello():
    if request.headers.get('a') == 'Acess-Control-Allow-Origin':
        return jsonify(trello_data), 200
    return jsonify(trello_data), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
