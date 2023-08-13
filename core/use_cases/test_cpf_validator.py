from ..use_cases.cpf_validator import CpfValidator
import pytest

@pytest.mark.parametrize('cpf, result',
    [
        ("1234567890123", True),
        ("3210987654321", True)
    ]                     
)
def test_cpf_valido(cpf, result):
    assert CpfValidator(cpf) == result
