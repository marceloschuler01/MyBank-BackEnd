from transacao.application.transacao_application import TransacaoApplication
from conta.application.conta_application import ContaApplication
from core.entity.conta import Conta
from conta.repository.conta_repository import ContaRepository
from Infra.utilities.with_db_connection import with_db_connection
from Infra.utilities.convert_to_dto import ConvertToDTO
from transacao.dto.transacao_dto import TransacaoDTO
from datetime import datetime

class UsecaseNewTransaction:
    def __init__(self, id_cliente: int):
        self._id_cliente = id_cliente
        self._origin_account: Conta
        self._destiny_account: Conta
        self._value: float
    
    @with_db_connection
    def new_transaction(self, id_destiny_account: int, value: float, conn=None) -> TransacaoDTO:

        self._get_origin_account(conn=conn)
        self._get_destiny_account(id_destiny_account=id_destiny_account, conn=conn)
        self._validate_value(value)

        self._move_the_money()
        result = self._save_transaction(conn=conn)

        return result

    def _get_origin_account(self, conn):

        api_conta = ContaApplication(id_cliente=self._id_cliente)
        self._origin_account = api_conta.get_(first=True, conn=conn)
    
    def _get_destiny_account(self, id_destiny_account: int, conn):

        conta_repository = ContaRepository()
        self._destiny_account = conta_repository.select_by_id(id=id_destiny_account, conn=conn)

    def _validate_value(self, value: float):
        self._value = value

    def _move_the_money(self):

        self._origin_account.saldo -= self._value
        self._destiny_account.saldo += self._value

    def _save_transaction(self, conn):

        current_date = self._get_current_date()

        transaction_data = {
            'id_conta_origem': self._origin_account.id,
            'id_conta_destino': self._destiny_account.id,
            'valor': self._value,
            'data_transacao': current_date,
        }

        transacao_application = TransacaoApplication()
        result = transacao_application.add_(data=transaction_data, conn=conn)
        result = ConvertToDTO(TransacaoDTO).convert(result)
        return result
    
    def _get_current_date(self) -> datetime:
        return datetime.now()

