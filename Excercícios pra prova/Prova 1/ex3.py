livro = 24.95 * (1 - 0.35)

x = int(input('Quantidade de cópias: '))

if x == 1 :
  custo = livro + 3
  print(f'O custo total foi de {custo:.2f}')
else :
  custo = (livro * x) + 3 + ((x - 1) * 0.75)
  print(f'O custo total foi de {custo:.2f}')


