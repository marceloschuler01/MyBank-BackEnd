from Infra.config.base import Base
from sqlalchemy import Column, String, Integer

class Agencia(Base):
    __tablename__ = "agencia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"Agencia (id={self.id}, , nome={self.nome})"
