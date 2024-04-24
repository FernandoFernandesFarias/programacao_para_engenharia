import math

cateto1 = float(input('Digite o valor do cateto 1: '))
cateto2 = float(input('Digite o valor do cateto 2: '))

hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

print(f'O valor da hipotenusa é de {hipotenusa:.2f}')