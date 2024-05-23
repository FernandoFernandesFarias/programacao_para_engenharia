import os, time

funcionarios = {}

def cadastroFuncionario():
  i = 0
  while i < 4:
    indiceNumerico = int(input('Digite o índice numérico do funcionário: '))
    nome = input('Digite o nome do funcionário: ')
    funcao = input('Digite a função do funcionário: ')
    tempoDeServico = int(input('Digite o tempo de serviço: '))

    contratados = []
    contratados.append(nome)
    contratados.append(funcao)
    contratados.append(tempoDeServico)
    funcionarios.update({indiceNumerico: contratados})
    i += 1
    os.system('cls' if os.name == 'nt' else 'clear')
  os.system('cls' if os.name == 'nt' else 'clear')
      
def demitiFuncionario():
  print(f'Qual funcionário você deseja demitir? \n')

  for funcionario in funcionarios.items():
    print(f'{funcionario}')

  opcao = int(input('Digite o código do funcionário que deseja demitir: '))

  if funcionarios[opcao][1] == 'Programador' or funcionarios[opcao][2] >= 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Não pode demitir esse funcionário')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    demitiFuncionario()
  else:
    funcionarios.pop(opcao)
    os.system('cls' if os.name == 'nt' else 'clear')
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
          print(
              '1 - Contratar funcionários \n'
              '2 - Demitir funcionários \n'
              '3 - Apresentar funcionários \n'
          )
          escolha = int(input('Digite de acordo com a opção desejada: '))

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
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Não tem funcionário para demitir.')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        demitiFuncionario()
        menu()

    case 3: 
      os.system('cls' if os.name == 'nt' else 'clear')
      if funcionarios == {}:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Não tem funcionário para apresentar.')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
      else:
        os.system('cls' if os.name == 'nt' else 'clear')
        apresentaFuncionario()
        menu()

menu()


