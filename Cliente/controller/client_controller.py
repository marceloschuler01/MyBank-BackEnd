from Infra.adapters.http_context import HttpContext
from Cliente.repository.cliente_repository import ClienteRepository
from Cliente.usecases.get_all_clientes import GetAllClientes
from Cliente.usecases.add_client import AddClient
from Cliente.usecases.get_client_by_id import GetClientById
from core.exceptions.invalid_date_exception import InvalidDate
from Infra.utilities.make_response import make_response
import logging

class ClientController:
    def __init__(self, http_context: HttpContext):
        self.clienteRepository = ClienteRepository()
        self.log = logging.getLogger(__name__)

    def add(self):
        try:
            self.__try_add()
        except InvalidDate as e:
            self.__error_handler(e)
        except Exception as e:
            logging.error("Não foi possível adicionar o cliente: "+str(e))
            self.http_context.make_response(body="Unsupported Media Type", status=415)
        finally:
            return self.http_context.response
    
    @make_response
    def get(self, id):
        cliente = GetClientById(self.clienteRepository).get(id=id)
        return {
            'status': 200,
            'body': cliente,
            }

    def __try_add(self):
        client_info = self.http_context.get_request()['body']
        AddClient(client_info, self.clienteRepository)
        self.http_context.make_response(body="Cliente Adicionado Com Sucesso", status=200)

    def __error_handler(self, e):
        self.log.error(e.msg)
        self.http_context.make_response(body=e.msg, status=400)