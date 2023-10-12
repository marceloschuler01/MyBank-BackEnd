import logging
from flask import Flask, request, session
from flask_cors import CORS
from flask_restful import Resource, Api

import sys

sys.path.append('C:\\Users\\Marcelo\\Desktop\\ufsc\\Estudos\\Projeto Banco\\BackEndMyBank')

app = Flask(__name__)
api = Api(app)

cors = CORS(app)

app.secret_key = '523a4792a759d43a53e2021ae86a0ccbb182bd9efde9fb2d22893252b0313207'


from resource.login_resource import LoginResource
api.add_resource(LoginResource, '/loginService')

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='../log/program.log'
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    app.run(port=3500, debug=True)