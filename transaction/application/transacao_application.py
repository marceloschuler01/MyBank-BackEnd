from core.application.application import Application
from core.models.transacao_model import TransacaoModel
from core.entity.transacao import Transacao
from transaction.repository.transacao_repository import TransacaoRepository

class TransacaoApplication(Application):
    def __init__(self, id_cliente=None):
        super().__init__(
            model=TransacaoModel, 
            entity=Transacao,
            repository=TransacaoRepository(),
            id_cliente=id_cliente
        )
