from flask_restful import Resource
from flask import session, request
from controller.client_controller import ClientController
from Infra.adapters.flask_adapter import FlaskRequestAdapter
from Infra.utilities.client_login_required import client_login_required

class ClienteResource(Resource):

    @client_login_required
    def get(self):
        return ClientController(FlaskRequestAdapter(request)).get_by_id(session['id'])