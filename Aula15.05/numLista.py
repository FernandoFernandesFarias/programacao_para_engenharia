numeros = []

def adicionaItem():
  while True:
    numeros.append(int(input('Digite um número para adicionar na lista: ')))
    opcao = input('S - Para sair. C - Para continuar: ').upper()
    if opcao == 'S':
      break

def verificaNum(n):
  if numeros.count(n) >= 1:
    return True
  else:
    return False

def main():
  adicionaItem()
  num = int(input('Digite um número: '))
  print(verificaNum(num))

if __name__ == '__main__':
  main()