from Infra.config.base import Base
from sqlalchemy import Column, Integer, FLOAT, ForeignKey, String
from core.entity.agencia import Agencia

class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(Integer)
    saldo = Column(FLOAT, default=0.0)
    id_cliente = Column(Integer, ForeignKey("cliente.id_cliente"))
    id_agencia = Column(Integer, ForeignKey(Agencia.id))

    def __repr__(self):
        return f"Conta (id={self.id}, cliente={self.id_cliente}, tipo={self.tipo}, saldo={self.saldo}, agencia={self.id_agencia})"
