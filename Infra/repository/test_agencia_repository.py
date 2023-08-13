from .agencia_repository import AgenciaRepository
from .connection_handler_mock import ConnectionHandlerMock

repo = AgenciaRepository(ConnectionHandlerMock)

def test_select_all():
    result = repo.select_all()
    assert str(result[0]) == 'Agencia (id=1, , nome=Trindade)'

'''def test_select_by_id():
    result = repo.select_by_id(1)
    assert str(result) == 'Agencia (id=1, , nome=Trindade)'''