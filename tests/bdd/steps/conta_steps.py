from behave import given, when, then
from src.models.conta import Conta


@given("uma conta com saldo de {saldo:d} reais")
def step_criar_conta(context, saldo):
    context.conta = Conta(numero="001", titular="João", saldo=saldo)
    context.erro = None


@when("eu depositar {valor:d} reais")
def step_depositar(context, valor):
    context.conta.depositar(valor)


@when("eu sacar {valor:d} reais")
def step_sacar(context, valor):
    context.conta.sacar(valor)


@when("eu tentar sacar {valor:d} reais")
def step_tentar_sacar(context, valor):
    try:
        context.conta.sacar(valor)
    except ValueError as e:
        context.erro = str(e)


@then("o saldo deve ser {esperado:d} reais")
def step_verificar_saldo(context, esperado):
    assert context.conta.saldo == esperado, (
        f"Esperado {esperado}, mas foi {context.conta.saldo}"
    )


@then("deve ocorrer um erro de saldo insuficiente")
def step_verificar_erro(context):
    assert context.erro == "Saldo insuficiente", (
        f"Erro esperado não ocorreu. Erro atual: {context.erro}"
    )
