x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

while x == y:
    print("Digite valores diferentes.")
    x = float(input("Digite o novo valor de x: "))
    y = float(input("Digite o novo valor de y: "))

z = ((x ** 2) + (y ** 2)) / (x - y)
print(z)
