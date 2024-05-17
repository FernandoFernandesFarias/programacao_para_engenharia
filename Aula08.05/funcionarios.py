import os, time

funcionarios = {}

def cadastroFuncionario():
  i = 0
  cod = 0
  while i < 4:
    nome = input('Digite o nome do funcionário: ')
    cod += 1
    funcionarios[cod]=nome
    i += 1
  os.system('cls' if os.name == 'nt' else 'clear')
  
def demitiFuncionario():
  print(f'Qual funcionário você deseja demitir? \n')

  for funcionario in funcionarios.items():
    print(f'{funcionario}')

  opcao = int(input('Digite o código do funcionário que deseja demitir: '))
  funcionarios.pop(opcao)
  print('Funcionário demitido')
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')

def apresentaFuncionario():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('----- LISTA DE FUNCIONÁRIOS ------')
  for funcionario in funcionarios.items():
    print(f'{funcionario}')
    print('------------------')

def menu():    
  def verificaOpcao():
    while True:
      try:
          print('///////////// Digite a opção desejada /////////////')
          escolha = int(input(
              '1 - Contratar funcionários \n'
              '2 - Demitir funcionários \n'
              '3 - Apresentar funcionários \n'
          ))

          if escolha not in range(1, 4):
              os.system('cls' if os.name == 'nt' else 'clear') 
              print('Digite um valor válido')  
          else:
              return escolha
      except ValueError:
          os.system('cls' if os.name == 'nt' else 'clear') 
          print('Digite um valor válido')
  
  opcao = verificaOpcao()
    
  match opcao:
    case 1: 
      os.system('cls' if os.name == 'nt' else 'clear')
      if funcionarios == {}:
        cadastroFuncionario()
        menu()
      else:
        print('Não tem como cadastrar novos funcionários.')
        menu()
    case 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      if funcionarios == {}:
        print('Não tem funcionário para demitir.')
        menu()
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        demitiFuncionario()
        menu()
    case 3: 
      os.system('cls' if os.name == 'nt' else 'clear')
      if funcionarios == {}:
        print('Não tem funcionário para apresentar.')
        menu()
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        apresentaFuncionario()
        menu()

menu()


