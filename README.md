# Tarefa de Familiarização: Estatísticas de Notas (Correção de Código)

**Tempo estimado:** 15 minutos | **Linguagem:** Python 3.8+ | **Tipo:** Correção de código (debug)

## Descrição da tarefa

Uma escola escreveu a função `estatisticas_notas(notas)` em `src/estatisticas_notas.py`.
Ela recebe a lista de notas de uma turma e deve retornar a **média**, a **maior nota**,
a **menor nota** e a **quantidade de aprovados**.

A função **não funciona como deveria**. Sua tarefa é **encontrar e corrigir os bugs**
sem reescrever a função do zero.

## Lista de requisitos

1. A função deve se chamar `estatisticas_notas` e receber um único parâmetro: `notas`, uma lista de números.
2. O retorno deve ser uma tupla `(media, maior, menor, aprovados)`.
3. `media` é a soma de todas as notas dividida pela quantidade de notas.
4. `maior` é a maior nota da lista e `menor` é a menor nota da lista.
5. Um aluno está **aprovado** se a nota for **maior ou igual a 6**. `aprovados` é a quantidade de alunos aprovados.
6. Se a lista for vazia, a função deve retornar `(0, 0, 0, 0)` sem lançar erro.

## Critérios de conclusão

A tarefa está concluída quando:

1. O teste `test_turma_com_varias_notas` passa.
2. O teste `test_lista_vazia` passa.
3. O comando `pytest` termina sem falhas (`2 passed`).
4. A função continua com o mesmo nome e a mesma assinatura (`estatisticas_notas(notas)`).
5. Os arquivos da pasta `tests/` não foram alterados.
6. A correção usa apenas `for`, `if` e operações básicas, sem bibliotecas externas.

## Exemplos de entrada e saída

| Entrada | Saída esperada |
|---------|----------------|
| `estatisticas_notas([7, 5, 10, 6])` | `(7.0, 10, 5, 3)` |
| `estatisticas_notas([4, 5, 3])` | `(4.0, 5, 3, 0)` |
| `estatisticas_notas([6, 6, 6])` | `(6.0, 6, 6, 3)` |
| `estatisticas_notas([8])` | `(8.0, 8, 8, 1)` |
| `estatisticas_notas([])` | `(0, 0, 0, 0)` |

## Restrições

- Cada nota é um número (`int` ou `float`) entre 0 e 10.
- A lista tem no máximo 100 notas.
- Não é permitido usar bibliotecas externas na solução (`statistics`, `numpy` etc.).
- Não é permitido usar as funções `max()`, `min()` e `sum()`.
- Não altere os arquivos da pasta `tests/`.

## Como executar

```bash
pip install -r requirements.txt
pytest
```

Antes da correção, os dois testes devem falhar. Ao final, ambos devem passar.
