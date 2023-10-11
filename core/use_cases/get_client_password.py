from ..repository.cliente_repository_interface import ClienteRepositoryInterface as ClienteRepository
from .convert_clients_to_DTO import ConvertClientsToDTO

class GetClientPassword:
    def __init__(self, cliente_repository: ClienteRepository) -> None:
        self.__repository = cliente_repository

    def get_by_cpf(self, cpf):
        cliente = self.__repository.select_by_cpf(cpf)
        password = cliente.senha
        return password