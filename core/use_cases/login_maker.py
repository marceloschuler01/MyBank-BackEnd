import logging
from ..repository.cliente_repository_interface import ClienteRepositoryInterface as ClienteRepository
from .get_client_password import GetClientPassword

class LoginMaker:
    def __init__(self, client_info: dict, repository: ClienteRepository):
        self.__repository = repository
        self.__cliente_info = client_info
        self.__cpf: str = None
        self.__nome: str = None
        self.log = logging.getLogger(__name__)

    def login(self):
        return self.__try_login()

    def __try_login(self):
        cpf = self.__cliente_info['cpf']
        passed_password = self.__cliente_info['password']
        password = GetClientPassword(self.__repository).get_by_cpf(cpf)
        correct_password = (passed_password == password)
        return correct_password
