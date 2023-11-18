from core.repository.repository_interface import RepositoryInterface
from Infra.utilities.data_validator import DataValidator
from Infra.utilities.with_db_connection import with_db_connection
from Infra.exceptions.duplicated_entry import DuplicatedEntry
from Infra.exceptions.bad_request import BadRequest
from core.models.model_interface import ModelInterface

class Application:
    def __init__(self, model: ModelInterface, entity, repository:RepositoryInterface=None, id_client:int=None):
        self._repository = repository
        self._model = model
        self._entity = entity
        self._id_client = id_client

    @with_db_connection
    def get_by_id_(self, id:int=None, conn=None, *args, **kwargs):
        self._repository.select_by_id(id=id, conn=conn, *args, **kwargs)

    @with_db_connection
    def get_(self, conn=None, filter:dict=dict()):
        filter['id_client'] = self._id_client
        self._repository.select(filter=filter, conn=conn)

    @with_db_connection
    def add_(self, data: dict, conn=None):
        dv = DataValidator(self._model)
        data = dv.validate(data=data)
        entity = self._entity(**data)

        try:
            result = self._repository.insert(entity=entity)
        except DuplicatedEntry:
            value = self._make_duplicate_entry_message(data=data)
            raise BadRequest(message='Duplicated Entry', value=value)
        return result

    def _make_duplicate_entry_message(self, data: dict) -> str:
        response = {}
        for column in self._model.columns_to_define_unicity:
            response = {column: data[column]}
        return response
