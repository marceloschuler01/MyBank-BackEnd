from cliente.application.client_application import ClienteApplication
from cliente.utilities.convert_clients_to_DTO import ConvertClientsToDTO
from Infra.utilities.with_db_connection import with_db_connection

class GetClientById:
    def __init__(self, id_cliente) -> None:
        self._id_cliente = id_cliente

    @with_db_connection
    def get(self, conn=None):
        application = ClienteApplication(id_cliente=self._id_cliente)
        cliente = application.get_(first=True, conn=conn)
        clientesDTO = ConvertClientsToDTO().convert(cliente)
        return clientesDTO