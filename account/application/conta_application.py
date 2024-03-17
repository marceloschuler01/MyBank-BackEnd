from core.application.application import Application
from core.models.conta_model import ContaModel
from core.entity.conta import Conta
from account.repository.conta_repository import ContaRepository

class ContaApplication(Application):
    def __init__(self, id_cliente=None):
        super().__init__(
            model=ContaModel, 
            entity=Conta,
            repository=ContaRepository(),
            id_cliente=id_cliente
        )
