from Infra.config.connection import DBConnectionHandler
from Infra.entity.cliente import Cliente
import logging

class ClienteRepository:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def select_all_clientes(self) -> list:
        with DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).all()
            return cliente
        
    def select_cliente_by_id(self, id: int) -> Cliente:
        with DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).get(id)
            return cliente

    def select_cliente_by_cpf(self, cpf: str) -> Cliente:
        with DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).filter(Cliente.cpf==cpf).first()
            return cliente

    def insert_cliente(self, cliente: Cliente) -> None:
        with DBConnectionHandler() as db:
            db.session.add(cliente)
            db.session.commit()
            self.log.info('Cliente adicionado com sucesso')
