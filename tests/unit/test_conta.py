import pytest
from src.models.conta import Conta


def test_deve_criar_conta_com_saldo_inicial():
    conta = Conta("001", "João Silva", 100)

    assert conta.numero == "001"
    assert conta.titular == "João Silva"
    assert conta.saldo == 100

def test_deve_sacar_um_valor_numerico():
    conta = Conta("001", "João Silva", 100)
    saldo_atual = conta.sacar(30)

    assert saldo_atual == 70
    assert conta.saldo == 70

def test_deve_sacar_valor_positivo():
    conta = Conta("001", "João Silva", 100)

    with pytest.raises(ValueError):
        conta.sacar(-10)

def test_deve_sacar_valor_menor_do_que_saldo():
    conta = Conta("001", "João Silva", 100)

    with pytest.raises(ValueError):
        conta.sacar(10000)

def test_deve_sacar_valor_inteiro():
    conta = Conta("001", "João Silva", 100)

    with pytest.raises(TypeError):
        conta.sacar("10000")