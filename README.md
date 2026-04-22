# Aula Prática: Testes de Software

Repositório para acompanhar a aula prática de testes de software.

## Setup

1. Clone o repositório:
```bash
git clone <seu-repo>
cd aula-testes-software
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
aula-testes-software/
├── src/
│   ├── models/conta.py           # Entidade de domínio
│   ├── repositories/             # Acesso a dados (em memória)
│   └── services/                 # Regras de negócio
└── tests/
    ├── unit/                     # Testes unitários (sem dependências externas)
    └── integration/              # Testes de integração (service + repository)
```

## Rodando os Testes

Todos os testes:
```bash
pytest
```

Com cobertura de código:
```bash
pytest --cov=src
```

Apenas unitários:
```bash
pytest tests/unit/ -v
```

Apenas integração:
```bash
pytest tests/integration/ -v
```

## Roteiro da Aula

### Parte 1 — Testes Unitários (20 min)
Testar a classe `Conta` isoladamente, sem dependências externas.
- Arquivo: `tests/unit/test_conta.py`
- Conceitos: asserções, `pytest.raises`, isolamento

### Parte 2 — Testes de Integração (20 min)
Testar `ContaService` em conjunto com `ContaRepository`.
- Arquivo: `tests/integration/test_conta_service.py`
- Conceitos: fixtures, colaboração entre camadas

### Parte 3 — TDD (25 min)
Criar `calcular_taxa_transferencia()` seguindo o ciclo Red → Green → Refactor.
- Arquivo: `tests/unit/test_taxa_transferencia.py`
- Conceitos: escrever o teste antes do código, iterações curtas
