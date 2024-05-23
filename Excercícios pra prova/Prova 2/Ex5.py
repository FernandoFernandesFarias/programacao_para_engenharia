numeros = []

qtdNum = int(input('Digite a quantidade de número vai ter na Lista: '))

for i in range(qtdNum):
  numeros.append(int(input('Digite um número: ')))

print(f'Tamanho da lista: {qtdNum}')
print(f'Lista: {numeros}')

for num in numeros:
  if num % 2 == 1:
    numeros.remove(num)

print(f'Lista sem os ímpares: {numeros}')

