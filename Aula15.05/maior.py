def somaMaior(n1, n2, limite):
  soma = n1 + n2
  if soma > limite:
    return True
  else: 
    return False

def main():
  n1 = int(input('Digite número 1: '))
  n2 = int(input('Digite número 2: '))
  limite = int(input('Digite o valor limite: '))
  print(somaMaior(n1, n2, limite))

if __name__ == '__main__':
  main()