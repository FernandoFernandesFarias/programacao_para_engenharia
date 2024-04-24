print('************************************   \n CÁLCULO DE GRANDEZAS ELÉTRICAS \n************************************  ')

grandeza = int(input('1. Tensão (em Volt)\n'
                 '2. Resistência (em Ohm)\n'
                 '3. Corrente (em Ampere)\n'
                 ))

match grandeza:
  case 1: 
    r = float(input('Digite o valor da resistência: '))
    i = float(input('Digite o valor da corrente: '))
    t = r * i
    print(f'A tensão é {t}')
  case 2: 
    u = float(input('Digite o valor da tensão: '))
    i = float(input('Digite o valor da corrente: '))
    r = u / i
    print(f'A tensão é {r:.2f}')
  case 3: 
    u = float(input('Digite o valor da tensão: '))
    r = float(input('Digite o valor da resistência: '))
    i = u / r
    print(f'A tensão é {i:.2f}')
