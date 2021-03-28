import json

from flask import Flask
from flask_restplus import Api, Resource


from src.server.instance import server

app, api = server.app, server.api

jira_json_file = open(file='./files/jira_formatted.json')
trello_json_file = open(file='./files/trello_formatted.json')

# Lendo o arquivo como Json.
jira_data = json.load(jira_json_file)
trello_data = json.load(trello_json_file)

# Fechando o arquivo, visto que ele não é mais necessário.
jira_json_file.close()
trello_json_file.close()


@api.route('/datas')
class Dadoslist(Resource):
    def get(self,):
        return jira_data

    def post(self,):
        response = api.payload
        jira_data.append(response)
        return response, 200
