from flask_restful import Resource
from flask import session
from Infra.utilities.request_adapter_decorator import request_adapter
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.error_handler import error_handler 
from Infra.utilities.make_response import make_response
from conta.usecase.usecase_conta import UsecaseConta

class ContaResource(Resource):

    @client_login_required
    @error_handler
    @make_response
    def get(self, request=None):
        id_cliente = session['id']
        uc = UsecaseConta(id_cliente=id_cliente)
        result = uc.get()
        return {
            'status': 200,
            'body': result,
            }
