from flask import Flask, request
from flask_cors import CORS
from Infra.controller.client_controller import ClientController
from Infra.adapters.flask_adapter import FlaskRequestAdapter

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
    app.run()