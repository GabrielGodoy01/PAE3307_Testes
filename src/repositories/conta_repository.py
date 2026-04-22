class ContaRepository:
    def __init__(self):
        self._contas = {}

    def salvar(self, conta):
        self._contas[conta.numero] = conta
        return conta

    def buscar_por_numero(self, numero):
        return self._contas.get(numero)

    def listar_todas(self):
        return list(self._contas.values())
