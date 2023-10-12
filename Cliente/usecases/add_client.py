import logging
from core.repository.repository_interface import RepositoryInterface as Repository
from Cliente.exceptions.invalid_cpf_exception import InvalidCpfException
from core.exceptions.invalid_name_exception import InvalidNameException
from core.use_cases.cpf_validator import CpfValidator

class AddClient:
    def __init__(self, client_info: dict, repository: Repository):
        self.__repository = repository
        self.__client_info = client_info
        self.__nome = None
        self.__cpf = None
        self.log = logging.getLogger(__name__)

        self.__add_client()

    def __add_client(self) -> None:
        try:
            self.__try_add_client()
        except Exception as e:
            #logging.ERROR("Não foi possível adicionar o cliente: "+str(e))
            raise e

    def __try_add_client(self):
        self.__get_client_info()
        self.__repository.insert(self.__cpf, self.__nome)

    def __get_client_info(self):
        self.__get_name()
        self.__get_cpf()        

    def __get_name(self):
        self.__nome = self.__client_info['nome']
        self.__valida_nome()

    def __get_cpf(self):
        self.__cpf = self.__client_info['cpf']
        self.__valida_cpf()

    def __valida_nome(self) -> bool:
        if not isinstance(self.__nome, str):
            raise InvalidNameException

    def __valida_cpf(self) -> bool:
        try:
            CpfValidator(self.__cpf)
        except InvalidCpfException as e:
            self.log.warn(e.msg)
            raise InvalidCpfException("Cpf Inválido")