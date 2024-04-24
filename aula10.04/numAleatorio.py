from random import randint

max = 10
tentativas = 0
num_sorteado = randint(1, 100)
num = 0

while (tentativas < max) and (num_sorteado != num):  
    print(f'Você tem {max - tentativas}, chances!')
    num = int(input('Adivinhe o numero sorteado(1 a 100):'))

    if num > num_sorteado:
      print(f'Numero sorteado é menor que {num}')

    elif num < num_sorteado:
      print(f'Numero sorteado é maior que {num}')
    tentativas += 1
  
if num == num_sorteado:
    print(f'Parabéns, você acertou o numero sorteado'\
    f' em {tentativas} vezes!')
else:
    print(f'Não foi desta vez! {num_sorteado}')