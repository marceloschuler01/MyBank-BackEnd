from core.entity.agencia import Agencia
from faker import Faker

fake = Faker()

def test_agencia():
    nome = fake.name()
    agencia = Agencia(nome=nome)
    assert agencia.nome == nome