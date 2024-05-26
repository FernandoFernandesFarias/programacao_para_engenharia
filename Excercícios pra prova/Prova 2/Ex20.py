numeros = []
numerosImpares = []
somaPar = 0
qtdImpares = 0

for num in range(6):
  numeros.append(int(input(f'Digite o número {num + 1}: ')))

for numImpar in numeros:
  if numImpar % 2 != 0:
    numerosImpares.append(numImpar)

for numPar in numeros:
  if numPar % 2 == 0:
    somaPar += numPar

for num in numerosImpares:
  qtdImpares += 1

print('Números: ', numeros)
print('Números ímpares: ', numerosImpares)
print('Soma dos números pares: ', somaPar)
print('Quantidade de números ímpares: ', qtdImpares)


