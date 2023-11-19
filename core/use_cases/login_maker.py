import logging
from cliente.application.client_application import ClienteApplication
from cliente.usecases.get_client_by_cpf import GetClienteByCpf
from Infra.utilities.with_db_connection import with_db_connection
from Infra.exceptions.not_found_data_exception import NotFoundedDataException

class LoginMaker:
    def __init__(self):
        self._application = ClienteApplication()
        self.log = logging.getLogger(__name__)

    def login(self, cpf:str=None, password: str=None):
        try: 
            return self.__try_login(cpf=cpf, password=password)
        except NotFoundedDataException:
            return None

    @with_db_connection
    def __try_login(self, cpf, password, conn=None):
        cliente = GetClienteByCpf().get(cpf=cpf, conn=conn)
        actual_password = cliente.senha
        correct_password = (password == actual_password)
        if correct_password:
            id = cliente.id_cliente
            return id
        return None
