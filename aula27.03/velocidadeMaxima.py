maxPermitida = int(input('Velocidade máxima permitida na avenida '))
velocidade = int(input('Velocidade do motorista: '))

if velocidade - maxPermitida <= 0 :
  print(f'Velocidade normal')
elif velocidade - maxPermitida >= 1 and velocidade - maxPermitida <= 10 :
  print(f'O motorista terá que pagar R$85,13')
  print(f'Infração leve. Tomou 3 pontos na carteira')
elif velocidade - maxPermitida <= 30 :
  print(f'O motorista terá que pagar R$127,69')
  print(f'Infração média. Tomou 5 pontos na carteira')
else :
  print('O motorista terá que pagar 574,62')
  print(f'Infração gravíssima. Tomou 7 pontos na carteira')

