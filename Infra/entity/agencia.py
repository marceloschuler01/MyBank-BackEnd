from ..config.base import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Agencia(Base):
    __tablename__ = "agencia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)
    funcionarios = relationship("Funcionario", backref="funcionario", lazy="subquery")

    def __repr__(self):
        return f"Agencia (id={self.id}, , nome={self.nome})"
