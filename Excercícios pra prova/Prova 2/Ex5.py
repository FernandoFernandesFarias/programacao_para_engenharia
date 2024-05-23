numeros = []
numerosSemImpar = []

qtdNum = int(input('Digite a quantidade de números que vai ter na Lista: '))

for i in range(qtdNum):
  numeros.append(int(input(f'Digite o número {i + 1}: ')))

for num in numeros:
  numerosSemImpar.append(num)

for numImpar in numeros:
  if numImpar % 2 != 0:
    numerosSemImpar.remove(numImpar)

print(f'Tamanho da lista: {qtdNum}')
print(f'Lista: {numeros}')
print(f'Lista sem os ímpares: {numerosSemImpar}')

