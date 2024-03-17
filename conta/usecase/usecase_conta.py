from conta.application.conta_application import ContaApplication
from Infra.utilities.with_db_connection import with_db_connection
from Infra.utilities.convert_to_dto import ConvertToDTO
from conta.dto.conta_DTO import ContaDTO

class UsecaseConta:
    def __init__(self, id_cliente):
        self._id_cliente = id_cliente
    
    @with_db_connection
    def get(self, conn=None):

        application = ContaApplication(id_cliente=self._id_cliente)
        data = application.get_(conn=conn)
        result = ConvertToDTO(ContaDTO).convert(data)
        return result
