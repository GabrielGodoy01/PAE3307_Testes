import pytest
from src.repositories.conta_repository import ContaRepository
from src.services.conta_service import ContaService


@pytest.fixture
def service():
    repository = ContaRepository()
    return ContaService(repository)


def test_deve_criar_conta_e_salvar_no_repositorio(service):
    conta = service.criar_conta("001", "Maria Silva", 200)

    assert conta.numero == "001"
    assert conta.saldo == 200

    conta_salva = service.repository.buscar_por_numero("001")
    assert conta_salva is not None
    assert conta_salva.titular == "Maria Silva"


def test_deve_realizar_saque_e_atualizar_repositorio(service):
    service.criar_conta("001", "João Silva", 100)

    conta = service.realizar_saque("001", 30)

    assert conta.saldo == 70

    conta_atualizada = service.repository.buscar_por_numero("001")
    assert conta_atualizada.saldo == 70


def test_deve_transferir_entre_contas(service):
    service.criar_conta("001", "João Silva", 100)
    service.criar_conta("002", "Maria Santos", 50)

    origem, destino = service.transferir("001", "002", 30)

    assert origem.saldo == 70
    assert destino.saldo == 80

    assert service.repository.buscar_por_numero("001").saldo == 70
    assert service.repository.buscar_por_numero("002").saldo == 80


def test_nao_deve_transferir_quando_conta_nao_existe(service):
    service.criar_conta("001", "João Silva", 100)

    with pytest.raises(ValueError, match="Conta não encontrada"):
        service.transferir("001", "999", 30)
