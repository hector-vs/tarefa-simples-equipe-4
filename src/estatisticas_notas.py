def estatisticas_notas(notas):
    """Retorna (media, maior, menor, aprovados) de uma lista de notas.

    Esta função contém bugs. Encontre e corrija.
    """
    total = 0
    maior = notas[0]
    menor = 0
    aprovados = 0

    for nota in notas:
        total += nota
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        if nota > 6:
            aprovados += 1

    media = total / (len(notas) - 1)
    return (media, maior, menor, aprovados)