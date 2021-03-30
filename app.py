import json

from flask import Flask, jsonify, request

app = Flask(__name__)

# gerando lista de dados

jira_json_file = open(file='jira_formatted.json')
trello_json_file = open(file='trello_formatted.json')

# Lendo o arquivo como Json.
jira_data = json.load(jira_json_file)
trello_data = json.load(trello_json_file)

# Fechando o arquivo, visto que ele não é mais necessário.
jira_json_file.close()
trello_json_file.close()


dados = jira_data + trello_data


@app.route("/dados", methods=["GET"])
def jira():
    if request.method == "GET":
        return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)
