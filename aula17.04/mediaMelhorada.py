soma = 0
qtdP = 0
qtdN = 0

for i in range(1,6):
  n = float(input('Digite um número: '))
  soma += n
  media = soma / i

  if n < 0:
    qtdN += 1
  else:
    qtdP += 1

percentualP = (qtdP / i) * 100
percentualN = (qtdN / i) * 100

print('A soma é ',soma)
print('A média é ',media)
print('A quantidade de positivos é ',qtdP)
print('A quantidade de negativos é ',qtdN)
print('O percentual de negativos é ',percentualN)
print('O percentual de positivos é ',percentualP)