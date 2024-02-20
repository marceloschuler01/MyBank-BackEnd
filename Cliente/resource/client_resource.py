from flask_restful import Resource
from flask import session
from cliente.usecases.get_client_by_id import GetClientById
from Infra.utilities.request_adapter_decorator import request_adapter
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.error_handler import error_handler 
from Infra.utilities.make_response import make_response

class ClienteResource(Resource):

    @client_login_required
    @error_handler
    @make_response
    def get(self, request=None):
        cliente = GetClientById(id_cliente=session['id']).get()
        return {
            'status': 200,
            'body': cliente,
            }
