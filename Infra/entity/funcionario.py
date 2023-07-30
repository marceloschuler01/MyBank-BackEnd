from ..config.base import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String, nullable=False, unique=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date)
    salario = Column(Integer)
    id_agencia = Column(Integer, ForeignKey("agencia.id"))

    def __repr__(self):
        return f"Funcionario (id={self.id}, nome={self.nome}, cpf={self.cpf}, agencia={self.id_agencia})"