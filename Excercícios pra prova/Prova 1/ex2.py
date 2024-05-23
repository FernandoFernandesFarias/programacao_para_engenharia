import math

fv = float(input('Valor final: '))
n = float(input('Número de meses: '))
i = float(input('Rentabildade mensal: ')) / 100

pv = fv / math.pow((1 + i), n)

print(f'O valor do montante é {pv:.2f}')