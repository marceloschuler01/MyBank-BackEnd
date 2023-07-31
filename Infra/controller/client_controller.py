from ..repository.cliente_repository import ClienteRepository
from core.use_cases.get_all_clientes import GetAllClientes
import json

class ClientController:
    def __init__(self):
        self.clienteRepository = ClienteRepository()

    def get_all(self):
        clientes = GetAllClientes(self.clienteRepository).get()
        return json.dumps(clientes, default=vars)