from Infra.config.base import Base
from sqlalchemy import Column, String, Date, Integer

class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String, nullable=False, unique=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date)
    email = Column(String)
    senha = Column(String)

    def __repr__(self):
        return f"id={self.id_cliente}, cpf={self.cpf}, nome={self.nome}"


