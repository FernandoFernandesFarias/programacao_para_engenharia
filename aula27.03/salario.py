ganhoHora = float(input('Quantos você ganha por hora? '))
horaTrabalhadas = float(input('Quantas horas você trabalha por mês? '))

salarioBruto = ganhoHora * horaTrabalhadas

ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato

print(f'{salarioBruto:.2f}')
print(f'{ir:.2f}')
print(f'{inss:.2f}')
print(f'{sindicato:.2f}')
print(f'{salarioLiquido:.2f}')



