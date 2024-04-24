import math


raio = float(input('Digite o raio: '))

area = math.pi * raio ** 2

c = 2 * math.pi * raio

print(f'Área: {area:,.2f} | Perímetro: {c:,.2f}')