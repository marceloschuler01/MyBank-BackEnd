from flask import Flask, make_response, jsonify
from flask_cors import CORS
from Infra.controller.client_controller import ClientController

app = Flask(__name__)
cors = CORS(app)

@app.route('/client', methods=['get'])
def get_clients():
    clientes = ClientController().get_all()
    return clientes

if __name__=='__main__':
    app.run()