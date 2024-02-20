from dataclasses import dataclass
from datetime import datetime

@dataclass
class TransacaoDTO:
    id: int
    tipo: int
    id_conta_origem: int
    id_conta_destino: int
    valor: float
    data_transacao: datetime
