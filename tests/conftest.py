import pytest
from src.repositories.conta_repository import ContaRepository
from src.services.conta_service import ContaService


@pytest.fixture
def repository():
    return ContaRepository()


@pytest.fixture
def service(repository):
    return ContaService(repository)
