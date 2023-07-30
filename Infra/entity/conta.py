from ..config.base import Base
from sqlalchemy import Column, Integer

class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"Conta (id={self.id})"

