from core.entity.conta import Conta
from core.repository.repository import Repository
from Infra.utilities.with_db_connection import with_db_connection
import logging

class ContaRepository(Repository):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__(Conta, self.log)
