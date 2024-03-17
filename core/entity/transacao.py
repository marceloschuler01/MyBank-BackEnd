from Infra.config.base import Base
from sqlalchemy import Column, Integer, FLOAT, ForeignKey, String, Date

class Transacao(Base):
    __tablename__ = "transacao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_conta_origem = Column(Integer, ForeignKey("conta.id"))
    id_conta_destino = Column(Integer, ForeignKey("conta.id"))
    valor = Column(FLOAT)
    data_transacao = Column(Date)

    def __repr__(self):
        return f"Transacao (id={self.id}, id_conta_origem={self.id_conta_origem}, id_conta_destino={self.id_conta_destino}, valor={self.valor}, data_transacao={self.data_transacao})"
