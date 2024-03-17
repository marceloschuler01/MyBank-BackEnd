from core.repository.repository_interface import RepositoryInterface as Repository
from customer.utilities.convert_clients_to_DTO import ConvertClientsToDTO

class GetAllClientes:
    def __init__(self, cliente_repository: Repository) -> None:
        self.__repository = cliente_repository

    def get(self):
        clientes = self.__repository.select_all()
        clientesDTO = ConvertClientsToDTO().convert(clientes)
        return clientesDTO