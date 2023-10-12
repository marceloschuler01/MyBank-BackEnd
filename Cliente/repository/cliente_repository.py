from core.entity.cliente import Cliente
from core.repository.repository import Repository
from Infra.utilities.with_db_connection import with_db_connection
import logging

class ClienteRepository(Repository):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__(Cliente, self.log)

    @with_db_connection
    def insert(self, cpf: str, nome: str, conn=None) -> None:

        cliente = Cliente(cpf=cpf, nome=nome)
        self.__add_client_with_connection(cliente, conn=conn)

    
    def __add_client_with_connection(self, cliente: Cliente, conn):
        conn.session.add(cliente)
        conn.session.commit()
        self.log.info('Cliente adicionado com sucesso')
