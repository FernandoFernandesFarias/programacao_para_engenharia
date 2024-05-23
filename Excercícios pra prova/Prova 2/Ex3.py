medias = []
qtdmedias = 0

for i in range(3):
  print(f'Aluno {i + 1}')
  nota1 = float(input('Digite a nota 1: '))
  nota2 = float(input('Digite a nota 2: '))
  nota3 = float(input('Digite a nota 3: '))
  nota4 = float(input('Digite a nota 4: '))
  print('/////////////////////////////////////')
  medias.append((nota1 + nota2 + nota3 + nota4) / 4)

for mediasAlta in medias:
  if mediasAlta >= 7:
    qtdmedias += 1
  
print(f'A quantidade de alunos com média >= a 7 é {qtdmedias}')

  