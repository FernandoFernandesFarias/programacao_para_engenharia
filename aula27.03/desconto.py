compra = float(input('Valor: '))
desc = float(input('Desconto: ')) / 100

desc = 1 - desc

total = compra * desc

print(total)