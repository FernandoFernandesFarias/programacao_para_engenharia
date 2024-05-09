p1 = (7.0, 8.3, 10.0, 6.5, 9.3)
p2 = (8.5, 6.9, 5.0, 7.5, 9.8)

mediaT1 = 0
mediaT2 = 0

for i in range(5):
  mediaT1 += p1[i]
mediaT1 = mediaT1 / 5

for j in range(5):
  mediaT2 += p2[j]
mediaT2 = mediaT2 / 5

print(f'Turma 1: {mediaT1:.2f}')
print(f'Turma 2: {mediaT2:.2f}')

if mediaT2 > mediaT1:
  print('Média da turma 2 é melhor')
else:
  print('Média da turma 1 é melhor')