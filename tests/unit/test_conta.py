import pytest
from src.models.conta import Conta


def test_deve_criar_conta_com_saldo_inicial():
    conta = Conta("001", "João Silva", 100)