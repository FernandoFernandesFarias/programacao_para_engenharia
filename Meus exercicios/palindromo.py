palavraInvertida = ''
palavra = input('Digite uma palavra: ').upper()
palavra = palavra.replace('-',' ').replace(' ', '')


for i in range(len(palavra), 0, -1):
  palavraInvertida += palavra[i - 1]

if palavra == palavraInvertida :
  print('É palíndromo')
else:
  print('Não é palíndromo')

