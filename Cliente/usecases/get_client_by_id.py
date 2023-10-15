from core.repository.repository_interface import RepositoryInterface
from Cliente.repository.cliente_repository import ClienteRepository
from Cliente.utilities.convert_clients_to_DTO import ConvertClientsToDTO
from Infra.utilities.with_db_connection import with_db_connection

class GetClientById:
    def __init__(self, cliente_repository: RepositoryInterface=ClienteRepository()) -> None:
        self.__repository = cliente_repository

    @with_db_connection
    def get(self, id, conn=None):
        clientes = [self.__repository.select_by_id(id, conn=conn)]
        clientesDTO = ConvertClientsToDTO().convert(clientes)
        return clientesDTO