notas = []

for i in range(1,4):
  notas.append(float(input(f'Digite a nota do aluno {i}: ')))

media = sum(notas) / i 

print(f'Nota mais alta: {max(notas)}')
print(f'Nota mais alta: {min(notas)}')
print(f'Média: {media:.2f}')