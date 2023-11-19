from core.application.application import Application
from core.models.cliente_model import ClienteModel
from core.entity.cliente import Cliente
from cliente.repository.cliente_repository import ClienteRepository

class ClienteApplication(Application):
    def __init__(self, id_cliente=None):
        super().__init__(
            model=ClienteModel, 
            entity=Cliente,
            repository=ClienteRepository(),
            id_cliente=id_cliente
        )
