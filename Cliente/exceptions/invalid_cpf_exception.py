from core.exceptions.invalid_data_exception import InvalidData

class InvalidCpfException(InvalidData):
    def __init__(self, msg="Cpf Inválido"):
        super(InvalidCpfException, self).__init__(msg)