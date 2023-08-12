from core.exceptions.invalid_cpf_exception import InvalidCpfException

try:
    raise InvalidCpfException()
except InvalidCpfException:
    print("Invalido")