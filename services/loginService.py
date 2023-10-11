from flask import Flask, request, session, redirect, url_for
from flask_cors import CORS
import logging
import sys

sys.path.append('C:\\Users\\Marcelo\\Desktop\\ufsc\\Estudos\\Projeto Banco\\BackEndMyBank')

from Infra.controller.login_controller import LoginController
from Infra.adapters.flask_adapter import FlaskRequestAdapter

app = Flask(__name__)
cors = CORS(app)

app.secret_key = '523a4792a759d43a53e2021ae86a0ccbb182bd9efde9fb2d22893252b0313207'

def isLogged():
    return 'cpf' in session

@app.route('/', methods=['GET'])
def index():
    if 'cpf' in session:
        return f'Seja bem vindo {session["nome"]}'
    else:
        return 'Logue!'

@app.route('/loginService', methods=['POST'])
def login_service():
    response = LoginController(FlaskRequestAdapter(request)).login()
    if response.status == 200:
        print('login sucesso')
        session['cpf'] = request.json['cpf']
    return response

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='../log/program.log'
    )
    app.run(port=3500)