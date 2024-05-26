lista = []
listaSemRepetido = []

for i in range(20):
  lista.append(int(input(f'Digite o número {i + 1}: ')))

for j in lista:
  if j not in listaSemRepetido:
    listaSemRepetido.append(j)

print(lista)
print(listaSemRepetido)
