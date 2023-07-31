from ..cliente_repository import ClienteRepository

repo = ClienteRepository()

def test_select_all():
    result = repo.select_all()
    assert str(result[0]) == 'Cliente (id=1, cpf=1234, nome=Marcelo)'

def test_select_by_id():
    result = repo.select_by_id(3)
    assert str(result) == 'Cliente (id=3, cpf=765, nome=Lucas)'

def test_select_by_cpf():
    result = repo.select_by_cpf(5123)
    assert str(result) == 'Cliente (id=6, cpf=5123, nome=Joao)'