n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
n3 = float(input('Digite nota 3: '))

media = (n1 + n2 + n3) / 3

print(f'Sua media é {media:.2f}')

if media >= 7 :
  print('Parabéns! Sua média é alta.')
elif media >= 5 :
  print('Sua média é razoável.')
else :
  print('Sua média é baixa. É uma boa oportunidade para melhorar.')
