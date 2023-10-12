from core.exceptions.invalid_date_exception import InvalidDate

class InvalidCpfException(InvalidDate):
    def __init__(self, msg="Cpf Inválido"):
        super(InvalidCpfException, self).__init__(msg)