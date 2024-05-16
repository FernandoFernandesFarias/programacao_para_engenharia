def calculaMedia(n1, n2, n3):
  return (n1 + n2 + n3) / 3

def verificaMedia(media):
  if media > 6:
    print(f'Aprovado com média {media:.2f}')
  elif media > 4:
    print(f'Verificação Suplementar com média {media:.2f}')
  else:
    print(f'Reprovado com média {media:.2f}')

def main():
  n1 = float(input('Digite a nota 1: '))
  n2 = float(input('Digite a nota 2: '))
  n3 = float(input('Digite a nota 3: '))

  media = calculaMedia(n1, n2, n3)
  verificaMedia(media)

if __name__ == '__main__':
  main()  