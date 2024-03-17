from core.entity.cliente import Cliente
from core.repository.repository import Repository
from Infra.utilities.with_db_connection import with_db_connection
import logging

class ClienteRepository(Repository):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__(Cliente, self.log)
