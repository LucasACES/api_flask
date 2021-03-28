from flask import Flask
from flask_restplus import Api


class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='ProjetoGSW',
                       description='dados Trello e Jira',
                       doc='/doc',
                       )

    def run(self,):
        self.app.run(
            debug=False,
            host='0.0.0.0',
            port=5000,

        )


server = Server()
