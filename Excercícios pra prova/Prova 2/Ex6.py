p1 = []
p2 = []

qtdAluno = int(input('Digite a quantidade de alunos tem na turma: '))

print('--------- Prova 1 ---------')
for i in range(qtdAluno):
  p1.append(float(input(f'{i + 1}º nota: ')))

print('--------- Prova 2 ---------')
for j in range(qtdAluno):
  p2.append(float(input(f'{j + 1}º nota: ')))

mediaP1 = sum(p1) / qtdAluno
mediaP2 = sum(p2) / qtdAluno

print(f'A média da turma na prova 1 foi de {mediaP1:.2f}')
print(f'A média da turma na prova 2 foi de {mediaP2:.2f}')

if mediaP1 > mediaP2:
  print('A turma obteve melhor média na prova 1')
else:
  print('A turma obteve melhor média na prova 2')



