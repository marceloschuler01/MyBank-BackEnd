from Infra.config.connection import DBConnectionHandler
from core.entity.agencia import Agencia

class AgenciaRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Agencia).all()
            return data

    def select_by_id(self, id: int) -> Agencia:
        with DBConnectionHandler() as db:
            data = db.session.get(Agencia, id)
            return data