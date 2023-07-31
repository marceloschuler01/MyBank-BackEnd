from core.entity.cliente import Cliente
from faker import Faker

fake = Faker()

def test_usuario():
    nome = fake.name()
    cpf = fake.name()
    cliente = Cliente(nome=nome, cpf=cpf)
    assert cliente.nome == nome
    assert cliente.cpf == cpf