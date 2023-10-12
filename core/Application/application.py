from core.repository.repository_interface import RepositoryInterface as Repository
from Infra.utilities.with_db_connection import with_db_connection

class Application:
    def __init__(self, repository:Repository=None, id_client:int=None):
        self._repository = repository
        self._id_client = id_client

    @with_db_connection
    def get_by_id_(self, id:int=None, conn=None, *args, **kwargs):
        self._repository.select_by_id(id=int, conn=conn, *args, **kwargs)

    @with_db_connection
    def get_(self, conn=None, filter:dict=dict()):
        filter['id_client'] = self._id_client
        self._repository.select(filter=filter, conn=conn)
