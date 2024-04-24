nome = input('Nome do corretor: ')
qtdImoveis = int(input('Quantidade de imóveis vendidos: '))
valorTotal = float(input('Valor total vendido: '))

salarioFinal = 1500 + (qtdImoveis * 200) + valorTotal * 0.05

print(f'{nome} tem seu salário final de {salarioFinal:.2f}')

