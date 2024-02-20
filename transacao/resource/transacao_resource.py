from flask_restful import Resource, reqparse
from flask import session, request
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.make_response import make_response
from Infra.utilities.error_handler import error_handler
from transacao.usecase.usecase_transacao import UsecaseTransacao

parser_post = reqparse.RequestParser()
parser_post.add_argument(
    'data',
    type=dict,
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

    '''@client_login_required
    @error_handler
    @make_response
    def post(self):
        parse = parser_post.parse_args()
        data = parse['data']

        result = CreateRegister().add(data)
        if result['status'] == 200:
            session['id'] = result['value']

        return result'''