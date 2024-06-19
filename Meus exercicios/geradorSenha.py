import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation
caracteresPossiveis = list(caracteres)

senha = []

quantidadeCaracter = int(input('Quantidade de caracteres: '))

while quantidadeCaracter <= 7:
  print('A senha deve conter pelo menos 8 caracteres!')   
  quantidadeCaracter = int(input('Quantidade de caracteres: '))

for digito in range(quantidadeCaracter):
    senha.append(random.choice(caracteresPossiveis))

print(f'Senha gerada: {''.join(senha)}') 
