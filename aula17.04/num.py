inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor final: '))
soma = 0

for i in range(inicio, fim + 1):
  soma += i
  print(i)

print(soma)