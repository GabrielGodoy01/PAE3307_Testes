Feature: Operações de conta bancária
  Como titular de uma conta
  Quero realizar depósitos e saques
  Para gerenciar meu saldo

  Scenario: Depositar valor válido
    Given uma conta com saldo de 100 reais
    When eu depositar 50 reais
    Then o saldo deve ser 150 reais

  Scenario: Sacar valor dentro do saldo
    Given uma conta com saldo de 200 reais
    When eu sacar 80 reais
    Then o saldo deve ser 120 reais

  Scenario: Tentar sacar mais do que o saldo disponível
    Given uma conta com saldo de 50 reais
    When eu tentar sacar 100 reais
    Then deve ocorrer um erro de saldo insuficiente
