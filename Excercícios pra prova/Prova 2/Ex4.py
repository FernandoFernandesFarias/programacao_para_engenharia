lista1 = []
lista2 = []
lista3 = []

print('---------- Lista 1 ----------')
for i in range(5):
  lista1.append(int(input('Digite um número: ')))

print('---------- Lista 2 ----------')
for j in range(5):
  lista2.append(int(input('Digite um número: ')))

for k in range(5):
  lista3.append(lista1[k])
  lista3.append(lista2[k])

print('---------- Todas as listas ----------')
print(lista1)
print(lista2)
print(lista3)