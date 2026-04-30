import pytest

from src.models.conta import Conta


def test_cria_conta_com_dados_iniciais():
    """Verifica se o construtor guarda corretamente os dados informados."""
    conta = Conta(numero="001", titular="Maria", saldo=100)

    assert conta.numero == "001"
    assert conta.titular == "Maria"
    assert conta.saldo == 100


def test_cria_conta_com_saldo_padrao_zero():
    """Caso de borda importante: nenhuma quantia inicial informada."""
    conta = Conta(numero="002", titular="Carlos")

    assert conta.saldo == 0


def test_depositar_valor_positivo_atualiza_e_retorna_saldo():
    """Caso feliz: o deposito soma ao saldo e devolve o novo valor."""
    conta = Conta(numero="003", titular="Ana", saldo=100)

    saldo_atual = conta.depositar(50)

    assert saldo_atual == 150
    assert conta.saldo == 150


@pytest.mark.parametrize("valor_invalido", [0, -10])
def test_depositar_valor_nao_positivo_dispara_erro(valor_invalido):
    """Zero e negativo devem ser rejeitados para manter a regra de negocio."""
    conta = Conta(numero="004", titular="Pedro", saldo=100)

    with pytest.raises(ValueError, match="Valor deve ser positivo"):
        conta.depositar(valor_invalido)


def test_sacar_valor_valido_atualiza_e_retorna_saldo():
    """Caso feliz: saque dentro do saldo reduz o valor corretamente."""
    conta = Conta(numero="005", titular="Julia", saldo=200)

    saldo_atual = conta.sacar(80)

    assert saldo_atual == 120
    assert conta.saldo == 120


def test_sacar_valor_igual_ao_saldo_zera_a_conta():
    """Caso de borda: sacar tudo deve ser permitido."""
    conta = Conta(numero="006", titular="Rafael", saldo=90)

    saldo_atual = conta.sacar(90)

    assert saldo_atual == 0
    assert conta.saldo == 0


@pytest.mark.parametrize("valor_invalido", [0, -5])
def test_sacar_valor_nao_positivo_dispara_erro(valor_invalido):
    """Zero e negativo devem falhar antes mesmo da verificacao de saldo."""
    conta = Conta(numero="007", titular="Beatriz", saldo=100)

    with pytest.raises(ValueError, match="Valor deve ser positivo"):
        conta.sacar(valor_invalido)


def test_sacar_valor_maior_que_saldo_dispara_erro():
    """Caso de erro principal: nao permitir saldo negativo."""
    conta = Conta(numero="008", titular="Lucas", saldo=50)

    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta.sacar(51)


def test_falha_no_saque_nao_altera_o_saldo():
    """Mesmo com erro, o estado da conta deve permanecer consistente."""
    conta = Conta(numero="009", titular="Fernanda", saldo=50)

    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta.sacar(100)

    assert conta.saldo == 50
