notas_aluno = [7,4,5,8,9,4]


def soma_notas(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma

def media_notas(notas):
    return soma_notas(notas) / len(notas)


def classifica_aluno(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'


print(f'A soma das notas do aluno é {soma_notas(notas_aluno)} e a média é {media_notas(notas_aluno)} das {len(notas_aluno)} notas do aluno. O aluno está {classifica_aluno(media_notas(notas_aluno))}')

# python estruturado.py