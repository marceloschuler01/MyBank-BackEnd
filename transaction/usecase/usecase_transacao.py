from transaction.application.transacao_application import TransacaoApplication
from account.application.conta_application import ContaApplication
from Infra.utilities.with_db_connection import with_db_connection
from Infra.utilities.convert_to_dto import ConvertToDTO
from transaction.dto.transacao_dto import TransacaoDTO

class UsecaseTransacao:
    def __init__(self, id_cliente: int):
        self._id_cliente = id_cliente
    
    @with_db_connection
    def get(self, conn=None) -> list[TransacaoDTO]:

        api_conta = ContaApplication(id_cliente=self._id_cliente)
        conta = api_conta.get_(first=True, conn=conn)

        application = TransacaoApplication()
        data = application.get_(filter={}, id_conta=conta.id, conn=conn)
        result = ConvertToDTO(TransacaoDTO).convert(data)

        return result
