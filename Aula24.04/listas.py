lista1 = []
lista2 = []
lista3 = []

print('Lista 1')

while len(lista1) < 5:
  try:
    lista1.append(int(input('Digite um valor: ')))
  except ValueError:
    print('Somente números')

print('Lista 2')

while len(lista2) < 5:
  try:
    lista2.append(int(input('Digite um valor: ')))
  except ValueError:
    print('Somente números')

for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)

    