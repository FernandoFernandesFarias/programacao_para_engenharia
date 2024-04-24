import os

#Função para validar os números.
def obterNumeros():
  while True:
    try:
      numero1 = int(input("Digite um número: "))
      numero2 = int(input("Digite outro número número: "))
      return numero1, numero2
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
        print("Por favor, digite um número válido.")

num1, num2 = obterNumeros()

#Função para fazer a adição e retornar o resultado.
def adicao(num1, num2):
  os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
  soma = num1 + num2
  print(f'O resultado da soma é {soma}')

#Função para fazer a subtração e retornar o resultado.
def subtracao(num1, num2):
  os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
  subtracao = num1 - num2
  print(f'O resultado da subtração é {subtracao}')

#Função para fazer a multiplicação e retornar o resultado.
def multiplicao(num1, num2):
  os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
  multiplicao = num1 * num2
  print(f'O resultado da multiplição é {multiplicao}')

#Função para fazer a divisão e retornar o resultado.
def divisao(num1, num2):
  os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
  try:
    divisao = num1 / num2
    print(f'O resultado da divisão é {divisao:.2f}')
  except ZeroDivisionError:
    print('Não dá pra dividir por 0')

#Função principal, retorna todas a outras.
def menu():
  continua = True

  #Loop que continuará até o usuário decidir encerrar o programa.
  while continua:
    
    #Função para validar a opção escolhida.
    def verificaOpcao():
      while True:
        try:
          print('///////////// Digite a opção desejada /////////////')
          escolha = int(input(
            'Adição = 1 \n'
            'Subtração = 2 \n'
            'Multiplicação = 3 \n'
            'Divisão = 4 \n'
            'Sair = 5 \n'
          ))

          if escolha != range(1, 5):
            os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
            print('Digite um valor válido')   
            return escolha    
        except:
          os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
          print('Digite um valor válido')
    
    opcao = verificaOpcao()
    
    #Seleciona a opção conforme o usuário decidir.
    match opcao:
      case 1:
        adicao(num1, num2)
      case 2:
        subtracao(num1, num2)
      case 3:
        multiplicao(num1, num2)
      case 4:
        divisao(num1, num2)
      case 5:
        os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console.
        print('Fim do programa')
        continua = False

#Retorna a função principal, apresentando todos os dados.
menu()