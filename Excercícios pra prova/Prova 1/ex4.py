import math

x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

z = (math.pow(x, 2) + math.pow(y, 2)) / (x - y)

print(f'{z:.2f}')