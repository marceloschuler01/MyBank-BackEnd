from dataclasses import dataclass

@dataclass
class ContaDTO:
    id: int
    tipo: int
    saldo: float
    id_agencia: int
