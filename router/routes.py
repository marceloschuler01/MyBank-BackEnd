from flask import Flask, request
from flask_cors import CORS
from Infra.controller.client_controller import ClientController
from Infra.adapters.flask_adapter import FlaskRequestAdapter
import logging

app = Flask(__name__)
cors = CORS(app)

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
        filename='./Infra/log/program.log'
    )

    app.run()