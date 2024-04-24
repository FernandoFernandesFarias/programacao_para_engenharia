num = int(input('Digite um número: '))
fatorial = 1

for i in range(num, 1, -1):
  fatorial *= i

print(f'{fatorial}')
