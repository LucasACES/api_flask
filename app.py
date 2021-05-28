from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request, render_template
from controller.function import *
import os
import sys

sys.path.append('/apiGSW/model/funcoes')
sys.path.append('/apiGSW/view/')

app = Flask(__name__, template_folder='view/templates')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/data/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/data/<opcao>/", methods=["GET"])
@app.route("/data/<opcao>/<nome>/", methods=["GET"])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def statusbyprojeto(opcao, nome=''):
    if request.method == "GET":
        projeto = projet(opcao, nome)
    return projeto


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
