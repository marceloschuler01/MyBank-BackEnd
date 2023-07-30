from Infra.config.connection import DBConnectionHandler
from Infra.entity.agencia import Agencia

class AgenciaRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Agencia).all()
            return data