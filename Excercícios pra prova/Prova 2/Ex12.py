lista1 = []
lista2 = []
lista3 = []

print(10 * '-', 'Lista 1', 10 * '-')
for i in range(6):
  lista1.append(int(input(f'Digite o número {i + 1}: ')))

print(10 * '-', 'Lista 2', 10 * '-')
for j in range(6):
  lista2.append(int(input(f'Digite o número {j + 1}: ')))

for k in range(6):
  lista3.append(lista1[k] + lista2[k])

print(lista1)
print(lista2)
print(lista3)