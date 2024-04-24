import math


x1 = float(input('Digite o valor de x1: '))
y1 = float(input('Digite o valor de y1: '))
p1 = x1, y1

x2 = float(input('Digite o valor de x2: '))
y2 = float(input('Digite o valor de y2: '))
p2 = x2, y2

distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f'A distancia entre {p1} e {p2} é de {distancia:.2f}')