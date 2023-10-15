from core.entity.cliente import Cliente
from core.repository.repository import Repository
from Infra.utilities.with_db_connection import with_db_connection
import logging

class ClienteRepository(Repository):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__(Cliente, self.log)

    @with_db_connection
    def insert(self, cliente: Cliente, conn=None) -> None:

        conn.session.add(cliente)
        conn.session.flush()
        conn.session.expunge_all()
        self.log.info('Cliente adicionado com sucesso')
        self.log.info(cliente)
        return cliente
