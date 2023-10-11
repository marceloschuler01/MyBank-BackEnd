import logging
from flask import Flask, request, session
from flask_cors import CORS

import sys

sys.path.append('C:\\Users\\Marcelo\\Desktop\\ufsc\\Estudos\\Projeto Banco\\BackEndMyBank')

from Infra.controller.client_controller import ClientController
from Infra.adapters.flask_adapter import FlaskRequestAdapter

app = Flask(__name__)
cors = CORS(app)

app.secret_key = '523a4792a759d43a53e2021ae86a0ccbb182bd9efde9fb2d22893252b0313207'

def isLogged():
    return 'cpf' in session

@app.route('/', methods=['GET'])
def index():
    if isLogged():
        return ClientController(FlaskRequestAdapter(request)).get_by_cpf(session['cpf'])
    else:
        return {"message": "Not Logged", "status":401}

@app.route('/client', methods=['GET'])
def get_clients():
    clientes = ClientController(FlaskRequestAdapter(request)).get_all()
    return clientes

@app.route('/client', methods=['POST'])
def add_client():
    response = ClientController(FlaskRequestAdapter(request)).add()
    return response

@app.route('/teste', methods=['GET'])
def teste():
    return str(request.headers)

if __name__=='__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='./log/program.log'
    )

    app.run()