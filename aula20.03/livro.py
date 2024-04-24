x = int(input("Quantidade de cópias: "))

preco = 24.95 - (35 * 24.95)/100

if x == 1 :
    total = preco + 3
    print('O valor total é ', total)
else:
    total = (preco * x) + 3 + ((x - 1) * 0.75) 
    print('O valor total é ', total)

