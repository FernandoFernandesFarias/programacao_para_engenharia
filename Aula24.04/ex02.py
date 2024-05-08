lista = []

while len(lista) < 5:
  try:
    lista.append(int(input('Digite um valor: ')))
  except ValueError:
    print('Somente números')
    

print(lista)
print(lista[::-1])