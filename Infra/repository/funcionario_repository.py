from Infra.config.connection import DBConnectionHandler
from core.entity.funcionario import Funcionario
from core.entity.agencia import Agencia
import logging

class FuncionarioRepository:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def select_all(self) -> list:
        with DBConnectionHandler() as db:
            data = db.session\
                .query(Funcionario)\
                .join(Agencia, Funcionario.id_agencia == Agencia.id)\
                .with_entities(
                    Funcionario.cpf,
                    Funcionario.nome,
                    Agencia.nome
                )\
                .all()
            return data
        