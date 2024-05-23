import math

variancia = 0

vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

for i in range(len(vendas) + 1):
  pass

media = sum(vendas) / i

for j in vendas:
  variancia += ((j - media) ** 2) / i 

desvioPadrao = math.sqrt(variancia)

print(f'Média: {media:.2f}')
print(f'Variância: {variancia:.2f}')
print(f'Desvio Padrão: {desvioPadrao:.2f}')