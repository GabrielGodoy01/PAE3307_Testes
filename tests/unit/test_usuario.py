
from src.models.usuario import Usuario
import pytest


def test_nome_e_email_devem_existir():
    usuario = Usuario("João", "joao@gmail.com")

    assert usuario.nome == "João"
    assert usuario.email == "joao@gmail.com"

def test_email_deve_conter_arroba():
    usuario = Usuario("João", "joao@gmail.com")

    assert "@" in usuario.email

def test_nome_nao_pode_ser_vazio():
    usuario = Usuario("João", "joao@gmail.com")

    assert len(usuario.nome) > 0

def test_email_nao_contem_arroba():

    with pytest.raises(ValueError):
        usuario = Usuario("João", "gmail.com")