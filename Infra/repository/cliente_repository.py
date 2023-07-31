from Infra.config.connection import DBConnectionHandler
from core.entity.cliente import Cliente
from core.repository.cliente_repository_interface import ClienteRepositoryInterface
import logging

class ClienteRepository(ClienteRepositoryInterface):
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def select_all(self) -> list:
        with DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).all()
            return cliente
        
    def select_by_id(self, id: int) -> Cliente:
        with DBConnectionHandler() as db:
            cliente = db.session.get(Cliente, id)
            return cliente

    def select_by_cpf(self, cpf: str) -> Cliente:
        with DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).filter(Cliente.cpf==cpf).first()
            return cliente

    def insert(self, cliente: Cliente) -> None:
        with DBConnectionHandler() as db:
            db.session.add(cliente)
            db.session.commit()
            self.log.info('Cliente adicionado com sucesso')
