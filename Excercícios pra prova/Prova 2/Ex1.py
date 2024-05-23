numeros = []
i = 0

while True:
  numeros.append(float(input('Digite um número: ')))
  i += 1
  if numeros.count(-1) >= 1:
    break

  soma = sum(numeros)
  menor = min(numeros)
  maior = max(numeros)
  media = soma / i

print(f'A soma é {soma}')
print(f'O menor é {menor}')
print(f'O maior é {maior}')
print(f'A média é {media:.2f}')
