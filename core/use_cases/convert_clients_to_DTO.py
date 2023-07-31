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
            self.__convert_client(cliente)

    def __convert_client(self, cliente):
        cpf = cliente.cpf
        nome = cliente.nome
        clienteDTO = ClienteDTO(cpf, nome)
        self.__add_DTO_to_list(clienteDTO)

    def __add_DTO_to_list(self, clienteDTO):
        self.__clientesDTO.append(clienteDTO)