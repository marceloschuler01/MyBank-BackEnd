from ..exceptions.invalid_cpf_exception import InvalidCpfException

class CpfValidator:
    def __init__(self, cpf: str):
        self.__cpf = cpf
        self.valido = None

        self.__validate()


    def __validate(self):
        self.__valide_type()
        self.__validate_length()
        self.valido = True

    def __valide_type(self):
        if not isinstance(self.__cpf, str):
            raise InvalidCpfException("O cpf deve ser do tipo string!")
    
    def __validate_length(self):
        if len(self.__cpf) != 13:
            raise InvalidCpfException("O cpf deve conter 13 dígitos!")
