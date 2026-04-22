from src.models.conta import Conta


class ContaService:
    def __init__(self, repository):
        self.repository = repository

    def criar_conta(self, numero, titular, saldo_inicial=0):
        conta = Conta(numero, titular, saldo_inicial)
        return self.repository.salvar(conta)

    def realizar_saque(self, numero_conta, valor):
        conta = self.repository.buscar_por_numero(numero_conta)

        if not conta:
            raise ValueError("Conta não encontrada")

        conta.sacar(valor)
        self.repository.salvar(conta)

        return conta

    def realizar_deposito(self, numero_conta, valor):
        conta = self.repository.buscar_por_numero(numero_conta)

        if not conta:
            raise ValueError("Conta não encontrada")

        conta.depositar(valor)
        self.repository.salvar(conta)

        return conta

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.repository.buscar_por_numero(numero_origem)
        conta_destino = self.repository.buscar_por_numero(numero_destino)

        if not conta_origem or not conta_destino:
            raise ValueError("Conta não encontrada")

        conta_origem.sacar(valor)
        conta_destino.depositar(valor)

        self.repository.salvar(conta_origem)
        self.repository.salvar(conta_destino)

        return conta_origem, conta_destino
