from flask_restful import Resource
from flask import session, request
from controller.login_controller import LoginController
from Infra.adapters.flask_adapter import FlaskRequestAdapter
from Infra.utilities.client_login_required import client_login_required

class LoginResource(Resource):

    def post(self):
        response, id = LoginController(FlaskRequestAdapter(request)).login()
        if response.status == '200 OK':
            print('login sucesso')
            session['id'] = id
            return 'Logou'
        return 'Not possible to make login'