import math

pv = float(input('Digite o valor do investimento: '))
n = float(input('Número de meses: '))
i = float(input('Rentabildade mensal: ')) / 100

fv = pv * math.pow((1 + i), n)

print(f'O valor do montante é {fv:.2f}')