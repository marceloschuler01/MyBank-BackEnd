from ..repository.cliente_repository_interface import ClienteRepositoryInterface
from .convert_clients_to_DTO import ConvertClientsToDTO

class GetAllClientes:
    def __init__(self, cliente_repository: ClienteRepositoryInterface) -> None:
        self.__repository = cliente_repository

    def get(self):
        clientes = self.__repository.select_all()
        clientesDTO = ConvertClientsToDTO().convert(clientes)
        return clientesDTO