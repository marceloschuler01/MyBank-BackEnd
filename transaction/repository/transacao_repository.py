from core.entity.transacao import Transacao
from core.repository.repository import Repository
from Infra.utilities.with_db_connection import with_db_connection
import logging

class TransacaoRepository(Repository):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        super().__init__(Transacao, self.log)

    @with_db_connection
    def select(self, id_conta:int, filter: dict={}, first=False, conn=None):

        if first:
            data = conn.session.query(self._model).filter_by(**filter).filter((Transacao.id_conta_origem == id_conta) | (Transacao.id_conta_destino == id_conta)).first()
        else:
            data = conn.session.query(self._model).filter_by(**filter).filter((Transacao.id_conta_origem == id_conta) | (Transacao.id_conta_destino == id_conta)).all()
        return data
