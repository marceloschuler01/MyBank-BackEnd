from core.entity.cliente import Cliente
from core.repository.cliente_repository_interface import ClienteRepositoryInterface
import logging

class ClienteRepository(ClienteRepositoryInterface):
    def __init__(self, DBConnectionHandler):
        self.__DBConnectionHandler = DBConnectionHandler
        self.log = logging.getLogger(__name__)

    def select_all(self) -> list:
        with self.__DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).all()
            return cliente
        
    def select_by_id(self, id: int) -> Cliente:
        with self.__DBConnectionHandler() as db:
            cliente = db.session.get(Cliente, id)
            return cliente

    def select_by_cpf(self, cpf: str) -> Cliente:
        with self.__DBConnectionHandler() as db:
            cliente = db.session.query(Cliente).filter(Cliente.cpf==cpf).first()
            return cliente

    def insert(self, cpf: str, nome: str) -> None:
        with self.__DBConnectionHandler() as db:
            try:
                cliente = Cliente(cpf=cpf, nome=nome)
                self.__add_client_with_connection(cliente, db)
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def __add_client_with_connection(self, cliente: Cliente, db):
        db.session.add(cliente)
        db.session.commit()
        self.log.info('Cliente adicionado com sucesso')
