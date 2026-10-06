import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from estatisticas_notas import estatisticas_notas


def test_turma_com_varias_notas():
    # Cobre média, maior, menor e a regra de aprovação (nota 6 aprova)
    assert estatisticas_notas([7, 5, 10, 6]) == (7.0, 10, 5, 3)


def test_lista_vazia():
    # Cobre o caso de lista vazia
    assert estatisticas_notas([]) == (0, 0, 0, 0)