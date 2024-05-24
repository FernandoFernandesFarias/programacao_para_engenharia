x = int(input('Digite o valor de início: '))
y = int(input('Digite o valor de encerramento: '))

lista = []

for i in range(x, y + 1):
  lista.append(i)

print(lista)