qtdPar = 0

for i in range(0, 5):
  num = int(input('Digite um número: '))
  if num % 2 == 0:
    qtdPar += 1
print(f'A quantidade de números pares é: {qtdPar}')