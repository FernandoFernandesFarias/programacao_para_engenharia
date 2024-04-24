senhaCorreta = 987654
senha = int(input('Digite a senha do cofre: '))

while senhaCorreta != senha:
  print('Senha incorreta')
  senha = int(input('Digite a senha do cofre: '))

print('Cofre aberto')
