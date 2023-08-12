from ..DTO.cliente_DTO import ClienteDTO
from ..entity.cliente import Cliente

class ConvertClientsToDTO:
    def __init__(self):
        self.__clientes = []
        self.__clientesDTO = []

    def convert(self, clientes: list) -> ClienteDTO:
        self.__clientes = clientes
        self.__convertEachClient()
        return self.__clientesDTO
    
    def __convertEachClient(self):
        for cliente in self.__clientes:
            clienteDTO = self.__convert_client(cliente)
            self.__add_DTO_to_list(clienteDTO)

    def __convert_client(self, cliente) -> ClienteDTO:
        cpf = cliente.cpf
        nome = cliente.nome
        return ClienteDTO(cpf, nome)

    def __add_DTO_to_list(self, clienteDTO):
        self.__clientesDTO.append(clienteDTO)