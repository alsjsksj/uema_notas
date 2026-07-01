# Sistema de Notas — UEMA NET

Projeto de exemplo para a disciplina **ITMADS537 — Gestão da Qualidade e Teste de Software**.

Este sistema gerencia notas de alunos de uma turma fictícia.
Ele foi escrito de propósito com alguns problemas para você encontrar e corrigir!

## Estrutura

```
sistema-notas/
├── notas/
│   ├── aluno.py      # Classe Aluno
│   └── turma.py      # Classe Turma
└── tests/
    └── test_aluno.py # Testes (incompletos — você vai completar!)
```

## Como instalar

```bash
pip install -r requirements.txt
```

## Como rodar os testes

```bash
pytest tests/ -v
```

## Como verificar o estilo do código

```bash
flake8 notas/
```

## Como verificar a cobertura de testes

```bash
pytest --cov=notas --cov-report=term-missing
```

---

> Projeto criado para fins educacionais. UEMA NET — Polo Itapecuru-Mirim.
