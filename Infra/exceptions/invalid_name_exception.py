from Infra.exceptions.invalid_data_exception import InvalidData

class InvalidNameException(InvalidData):
    def __init__(self, msg="Nome Inválido"):
        super(InvalidNameException, self).__init__(msg)

