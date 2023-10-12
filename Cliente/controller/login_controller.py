import logging
import sys

sys.path.append('C:\\Users\\Marcelo\\Desktop\\ufsc\\Estudos\\Projeto Banco\\BackEndMyBank')

from Infra.config.connection import DBConnectionHandler
from Infra.adapters.http_context import HttpContext
from Cliente.repository.cliente_repository import ClienteRepository
from core.use_cases.login_maker import LoginMaker

class LoginController:
    def __init__(self, http_context: HttpContext):
        self.clienteRepository = ClienteRepository()
        self.http_context = http_context
        self.log = logging.getLogger(__name__)

    def login(self):
        login_info = self.http_context.get_request()['body']
        login = LoginMaker(login_info, self.clienteRepository).login()
        if login:
            self.http_context.make_response(status=200, body={"Pretty":"Login feito com Sucesso!"})
            return self.http_context.response, login
        self.http_context.make_response(status=401, body={"Pretty":"Usuário ou senha incorreta! "})
        return self.http_context.response, login