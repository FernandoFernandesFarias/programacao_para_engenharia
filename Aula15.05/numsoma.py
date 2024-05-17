def somaN(n):
  soma = 0
  for i in range(n, 0, -1):
    soma += i
  return soma

def main():
  numero = int(input('Digite um número: '))
  print(f'A soma de todos os números menores ou igual a {numero} é {somaN(numero)}')

if __name__ == '__main__':
  main()