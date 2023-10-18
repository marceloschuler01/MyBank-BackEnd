import logging
from core.repository.repository_interface import RepositoryInterface as Repository
from cliente.repository.cliente_repository import ClienteRepository
from core.exceptions.invalid_data_exception import InvalidData
from cliente.usecases.cpf_validator import CpfValidator
from core.entity.cliente import Cliente
from sqlalchemy.exc import IntegrityError
from Infra.utilities.with_db_connection import with_db_connection
from Infra.utilities.data_validator import DataValidator
from core.models.cliente_model import COLUMNS

class CreateRegister:
    def __init__(self, repository: ClienteRepository=ClienteRepository()):
        self._repository = repository
        self._client_: Cliente
        self._nome = None
        self._cpf = None
        self.log = logging.getLogger(__name__)

    def add(self, client_info) -> None:
        try:
            dv = DataValidator(COLUMNS)
            valido = dv.validate(client_info)
            if not valido == "Valido":
                return {'status': 400, 'body': valido, 'value': None}
            self._client = Cliente(**client_info)
            result = self._try_add_client()
            return {'status':200, 'body':str(result), 'value':result.id_cliente}
        except InvalidData as e:
            self.log.warn(str(e))
            return {'status': 400, 'body':e.msg, 'value': None}
        except IntegrityError as e:
            self.log.warn(str(e))
            return {'status': 400, 'body':str(e), 'value': None}

    def _try_add_client(self):
        self._validate_data()
        return self._repository.insert(self._client)

    def _validate_data(self):
        self._valida_cpf()
        self._valida_nome()

    def _valida_nome(self):
        pass

    def _valida_cpf(self):
        #CpfValidator(self._cpf)
        pass