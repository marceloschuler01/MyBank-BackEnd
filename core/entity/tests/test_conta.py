from faker import Faker
from ..conta import Conta

fake = Faker()

def test_conta_valida():
    id_cliente = 1
    id_agencia = 1
    tipo = 1
    conta = Conta(tipo=tipo, id_cliente=id_cliente, id_agencia=id_agencia)
    assert conta.id_agencia == id_agencia
    assert conta.id_cliente == id_cliente
    assert conta.tipo == tipo