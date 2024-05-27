num = int(input('Digite um número: '))
div = 0

for n in range(1, num):
  if num % n == 0:
    div += n

if num == div:
  print(f'{num} é um número perfeito')
else:
  print(f'{num} não é um número perfeito')
