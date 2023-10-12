import logging
from core.repository.repository_interface import RepositoryInterface as Repository
from .get_client_password import GetClientPassword
from Cliente.repository.cliente_repository import ClienteRepository
from Cliente.usecases.get_client_by_cpf import GetClienteByCpf
from Infra.utilities.with_db_connection import with_db_connection

class LoginMaker:
    def __init__(self, client_info: dict, cliente_repository: Repository):
        self.__repository = cliente_repository
        self.__cliente_info = client_info
        self.__cpf: str = None
        self.__nome: str = None
        self.log = logging.getLogger(__name__)

    def login(self):
        return self.__try_login()

    @with_db_connection
    def __try_login(self, conn=None):
        cpf = self.__cliente_info['cpf']
        passed_password = self.__cliente_info['password']
        password = GetClientPassword(self.__repository).get_by_cpf(cpf, conn=conn)
        correct_password = (passed_password == password)
        if correct_password:
            id = GetClienteByCpf(self.__repository).get(cpf=cpf, conn=conn).id_cliente
            print(id)
            return id
        return None
