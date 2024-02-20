from Infra.config.base import Base
from sqlalchemy import Column, Integer, FLOAT, ForeignKey, String, Date

class Transacao(Base):
    __tablename__ = "transacao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(Integer)
    id_conta_origem = Column(Integer, ForeignKey("cliente.id_conta"))
    id_conta_destino = Column(Integer, ForeignKey("cliente.id_conta"))
    valor = FLOAT
    data_transacao = Date

    def __repr__(self):
        return f"Transacao (id={self.id}, tipo={self.tipo}, id_conta_origem={self.id_conta_origem}, id_conta_destino={self.id_conta_destino}, valor={self.valor}, data_transacao={self.data_transacao})"
