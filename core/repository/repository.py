from core.repository.repository_interface import RepositoryInterface
from Infra.utilities.with_db_connection import with_db_connection
from Infra.utilities.verify_if_it_was_found_data import verify_if_it_was_found_data
from Infra.exceptions.duplicated_entry import DuplicatedEntry
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_

class Repository(RepositoryInterface):
    def __init__(self, model, log):
        self._model = model
        self.log = log

    @with_db_connection
    @verify_if_it_was_found_data
    def select_all(self, conn=None) -> list:
        data = conn.session.query(self._model).all()
        return data

    @with_db_connection
    def select(self, filter: dict={}, or_: dict={}, first=False, conn=None):

        if first:
            data = conn.session.query(self._model).filter_by(**filter).first()
        else:
            data = conn.session.query(self._model).filter_by(**filter).all()
        return data

    @with_db_connection
    def select_by_id(self, id: int, conn=None):
        data = conn.session.get(self._model, id)
        return data

    @with_db_connection
    def delete(self, data, conn=None):
        conn.session.delete(data)

    @with_db_connection
    def insert(self, entity, conn=None):
        try:
            conn.session.add(entity)
            conn.session.flush()
            conn.session.expunge_all()
        except IntegrityError as e:
            raise DuplicatedEntry(err=e)
        self.log.info('\n -- Data Added Successfully --')
        self.log.info(entity)
        return entity
