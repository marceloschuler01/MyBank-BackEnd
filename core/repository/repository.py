import logging
from core.repository.repository_interface import RepositoryInterface
from Infra.utilities.with_db_connection import with_db_connection
from Infra.utilities.verify_if_it_was_found_data import verify_if_it_was_found_data

class Repository(RepositoryInterface):
    def __init__(self, model, log):
        self.__model = model
        self.log = log

    @with_db_connection
    @verify_if_it_was_found_data
    def select_all(self, conn=None) -> list:
        data = conn.session.query(self.__model).all()
        return data

    @with_db_connection
    @verify_if_it_was_found_data   
    def select(self, filter: dict={}, conn=None):
        data = conn.session.query(self.__model).filter_by(**filter).first()
        return data

    @with_db_connection
    @verify_if_it_was_found_data
    def select_by_id(self, id: int, conn=None):
        data = conn.session.get(self.__model, id)
        return data

    '''    def insert(self, cpf: str, nome: str) -> None:
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
    '''