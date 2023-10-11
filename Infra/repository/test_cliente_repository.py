from .cliente_repository import ClienteRepository
from .connection_handler_mock import ConnectionHandlerMock

repo = ClienteRepository(ConnectionHandlerMock)

def test_select_all():
    result = repo.select_all()
    assert str(result[0]) == 'Cliente (id=1, cpf=123, nome=Joao)'

def test_insert():

    res = repo.insert(nome="aaaa", cpf="12444")
    assert res == None

'''def test_select_by_id():
    result = repo.select_by_id(1)
    assert str(result) == 'Cliente (id=1, cpf=123, nome=Joao)'''

'''def test_select_by_cpf():
    result = repo.select_by_cpf(5123)
    assert str(result) == 'Cliente (id=6, cpf=5123, nome=Joao)'''