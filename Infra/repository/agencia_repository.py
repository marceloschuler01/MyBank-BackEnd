import sys

sys.path.append('C:\\Users\\Marcelo\\Desktop\\ufsc\\Estudos\\Projeto Banco\\BackEndMyBank')

import logging
from core.entity.agencia import Agencia

class AgenciaRepository:
    def __init__(self, DBConnectionHandler):
        self.__DBConnectionHandler = DBConnectionHandler
        self.log = logging.getLogger(__name__)

    def select_all(self):
        with self.__DBConnectionHandler() as db:
            data = db.session.query(Agencia).all()
            return data

    def select_by_id(self, id: int) -> Agencia:
        with self.__DBConnectionHandle() as db:
            data = db.session.get(Agencia, id)
            return data
