soma = 0
maior = -1
menor = 9999999
i = 0
num = 0

while num >= 0 :
  i += 1
  num = int(input('Digite um número: '))
  
  if num >= 0 :
    soma = soma + num
    media = soma / i
    if menor > num :
      menor = num
    if maior < num :
      maior = num



print(f'A soma é {soma}')
print(f'A média da soma dos números é {media:.2f}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')


   