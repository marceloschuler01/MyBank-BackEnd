from customer.repository.cliente_repository import ClienteRepository
from Infra.utilities.with_db_connection import with_db_connection

class GetClienteByCpf:
    def __init__(self, repository=ClienteRepository()) -> None:
        self._repository = repository

    @with_db_connection
    def get(self, cpf, conn=None):
        cliente = self._repository.select(filter={'cpf':cpf}, first=True, conn=conn)
        return cliente
