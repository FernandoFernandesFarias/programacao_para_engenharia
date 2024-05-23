import math

r = float(input('Digite o raio: '))

c = 2 * math.pi * r
a = math.pi * math.pow(r, 2)

print(f'Perímetro: {c:.2f}')
print(f'Área: {a:.2f}')