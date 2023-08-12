from ..exceptions.invalid_date_exception import InvalidDate

class InvalidNameException(InvalidDate):
    def __init__(self, msg="Nome Inválido"):
        super(InvalidNameException, self).__init__(msg)

