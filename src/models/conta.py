class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= valor
        return self.saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")

        self.saldo += valor
        return self.saldo
