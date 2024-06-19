notas = []
alunos = {}
contadorFrequencia = 0

while True:
    codigo = int(input('Digite o código: '))
    if codigo == 0: 
        break
    nome = input('Nome do aluno: ')
    nota = float(input('Nota do aluno: '))
    frequencia = int(input('Frequência do aluno: '))
    aluno = [nome, nota, frequencia]
    alunos[codigo] = aluno

for codigo, aluno in alunos.items():
    notas.append(aluno[1])

    if aluno[1] == max(notas):
        alunoNotaAlta = (f'{aluno[0]} teve maior nota, {aluno[1]}. E frequência de {aluno[2]}')
    if aluno[1] == min(notas):
        alunoNotaBaixa = (f'{aluno[0]} teve menor nota, {aluno[1]}. E frequência de {aluno[2]}')

    if aluno[2] >= 50:
        contadorFrequencia += 1

print(alunoNotaAlta)
print(alunoNotaBaixa)
print(f'Quantidade de alunos com mais de 50 em frequência: {contadorFrequencia}')
