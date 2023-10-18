from flask_restful import Resource, reqparse
from flask import session, request
from Infra.adapters.flask_adapter import FlaskRequestAdapter
from Infra.utilities.client_login_required import client_login_required
from Infra.utilities.request_adapter_decorator import request_adapter
from Infra.utilities.make_response import make_response
from Infra.adapters.req_parser_adapter import ReqParserAdapter
from core.use_cases.login_maker import LoginMaker
from cliente.usecases.create_register import CreateRegister
from Infra.utilities.error_handler import error_handler
import logging

parser_post = reqparse.RequestParser()
parser_post.add_argument(
    'data',
    type=dict,
    required=True,
    help="Parameter Invalid",
)

class RegisterResource(Resource):

    @error_handler
    @make_response
    def post(self):
        parse = parser_post.parse_args()
        data = parse['data']

        result = CreateRegister().add(data)
        if result['status'] == 200:
            session['id'] = result['value']

        return result