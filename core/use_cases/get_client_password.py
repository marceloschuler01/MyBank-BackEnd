from core.repository.repository_interface import RepositoryInterface as Repository
from customer.utilities.convert_clients_to_DTO import ConvertClientsToDTO
from Infra.utilities.with_db_connection import with_db_connection

class GetClientPassword:
    def __init__(self, cliente_repository: Repository) -> None:
        self.__repository = cliente_repository

    @with_db_connection
    def get_by_cpf(self, cpf, conn=None):
        cliente = self.__repository.select(filter={'cpf':cpf}, conn=conn)
        password = cliente.senha
        return password