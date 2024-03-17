from flask_restful import Resource, reqparse
from flask import session, request
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.make_response import make_response
from Infra.utilities.error_handler import error_handler
from transaction.usecase.usecase_transacao import UsecaseTransacao
from transaction.usecase.usecase_new_transaction import UsecaseNewTransaction

parser_post = reqparse.RequestParser()
parser_post.add_argument(
    'id_destiny_account',
    type=int,
    required=True,
    help="Parameter Invalid",
)
parser_post.add_argument(
    'value',
    type=float,
    required=True,
    help="Parameter Invalid",
)

class TransacaoResource(Resource):

    @client_login_required
    @error_handler
    @make_response
    def get(self):
        
        uc = UsecaseTransacao(id_cliente=session['id'])
        result = uc.get()

        return {
            'status': 200,
            'body': result,
            }

    @client_login_required
    @error_handler
    @make_response
    def post(self):
        parse = parser_post.parse_args()
        id_destiny_account = parse['id_destiny_account']
        value = parse['value']

        uc = UsecaseNewTransaction(id_cliente=session['id'])
        result = uc.new_transaction(id_destiny_account=id_destiny_account, value=value)

        return {
            'status': 200,
            'body': result
            }
