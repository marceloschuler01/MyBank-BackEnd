from flask_restful import Resource
from flask import session, request
from Infra.adapters.flask_adapter import FlaskRequestAdapter
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.request_adapter_decorator import request_adapter
from Infra.utilities.make_response import make_response
from Infra.adapters.req_parser_adapter import ReqParserAdapter
from core.use_cases.login_maker import LoginMaker

parser_post = ReqParserAdapter.RequestParser()
parser_post.add_argument(
    'data',
    type=dict,
    required=True,
    help="Parameter Invalid",
)

class LoginResource(Resource):

    @make_response
    def post(self):
        parse = parser_post.parse_args()
        data = parse['data']
        id = LoginMaker(data).login()
        if id:
            session['id'] = id
            return {'status':200, 'body':{"Pretty":"Login feito com Sucesso!"}}
        return {'status':401, 'body':{"Pretty":"Usuário ou senha incorreta! "}}