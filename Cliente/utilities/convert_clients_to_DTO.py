from Cliente.dto.cliente_DTO import ClienteDTO
from core.entity.cliente import Cliente
from Infra.utilities.convert_to_dto import ConvertToDTO

class ConvertClientsToDTO(ConvertToDTO):
    def __init__(self):
        super().__init__(ClienteDTO)
