from core.repository.conta_repository_interface import ContaRepository
from Infra.config.connection import DBConnectionHandler
from core.entity.conta import Conta
import logging

class ContaRepository(ContaRepository):
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def select_all(self) -> list:
        with DBConnectionHandler() as db:
            data = db.session.query(Conta).all()
            return data
        
    def select_by_id(self, id: int) -> Conta:
        with DBConnectionHandler() as db:
            data = db.session.get(Conta, id)
            return data

    def insert(self, conta: Conta) -> None:
        with DBConnectionHandler() as db:
            db.session.add(conta)
            db.session.commit()
            self.log.info('Conta criada com sucesso')