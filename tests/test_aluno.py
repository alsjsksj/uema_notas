import pytest
from notas.aluno import Aluno


# ── Testes ja existentes ──────────────────────────────────────────────────

def test_criar_aluno():
    aluno = Aluno("Maria Silva", "2024001")
    assert aluno.nome == "Maria Silva"
    assert aluno.matricula == "2024001"
    assert aluno.notas == []


def test_adicionar_nota_valida():
    aluno = Aluno("Joao Santos", "2024002")
    aluno.adicionar_nota(8.0)
    assert 8.0 in aluno.notas


def test_adicionar_nota_invalida_acima_de_10():
    aluno = Aluno("Ana Costa", "2024003")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(11.0)


def test_calcular_media_com_duas_notas():
    aluno = Aluno("Pedro Lima", "2024004")
    aluno.adicionar_nota(6.0)
    aluno.adicionar_nota(8.0)
    assert aluno.calcular_media() == 7.0


# ── Adicione seus testes aqui embaixo ─────────────────────────────────────
# Dica: tente escrever testes para os metodos que ainda nao foram testados:
#   - adicionar_nota() com nota igual a 0 (valida) e nota negativa (invalida)
#   - calcular_media() sem nenhuma nota
#   - aprovado() com media acima de 5.0
#   - aprovado() com media IGUAL a 5.0  <-- esse vai te surpreender!
#   - situacao() retornando "Aprovado" e "Reprovado"
