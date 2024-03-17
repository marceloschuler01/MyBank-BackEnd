from flask_restful import Resource
from flask import session, request
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.make_response import make_response
from Infra.utilities.error_handler import error_handler
from Infra.adapters.req_parser_adapter import ReqParserAdapter
from core.use_cases.login_maker import LoginMaker

parser_post = ReqParserAdapter.RequestParser()
parser_post.add_argument(
    'cpf',
    type=str,
    required=True,
    help="Parameter Invalid Cpf",
)
parser_post.add_argument(
    'password',
    type=str,
    required=True,
    help="Parameter Invalid Password",
)

class LoginResource(Resource):

    @error_handler
    @make_response
    def post(self):
        parser = parser_post.parse_args()
        cpf = parser['cpf']
        password = parser['password']
        id = LoginMaker().login(cpf=cpf, password=password)
        if id:
            session['id'] = id
            return {'status':200, 'body':{"Pretty":"Login feito com Sucesso!"}}
        return {'status':401, 'body':{"Pretty":"Usuário ou senha incorreta! "}}