import logging
from ..repository.cliente_repository_interface import ClienteRepositoryInterface as ClienteRepository
from ..exceptions.invalid_cpf_exception import InvalidCpfException
from ..exceptions.invalid_name_exception import InvalidNameException

class AddClient:
    def __init__(self, client_info: dict, repository: ClienteRepository):
        self.__repository = repository
        self.__client_info = client_info
        self.__nome = None
        self.__cpf = None

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
        nome = self.__client_info['nome']
        self.__valida_nome(nome)
        self.__nome = nome

    def __get_cpf(self):
        cpf = self.__client_info['cpf']
        self.__valida_cpf(cpf)
        self.__cpf = cpf

    def __valida_nome(self, nome: str) -> bool:
        if not isinstance(nome, str):
            raise InvalidNameException

    def __valida_cpf(self, cpf: str) -> bool:
        if not isinstance(cpf, str):
            raise InvalidCpfException