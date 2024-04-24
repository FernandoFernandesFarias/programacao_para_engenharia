litros = float(input('Quantidade de litros vendidos: '))
tipo = input('Tipo de combustível: ')

match tipo :
  case 'A' :
    if litros >= 20 :
      valorPago = (4.98 * litros) * (1 - 0.05)
      print(f'O valor pago pelo cliente foi de {valorPago:.2f}') 
    else : 
      valorPago = (4.98 * litros) * (1 - 0.02)
      print(f'O valor pago pelo cliente foi de {valorPago:.2f}') 

  case 'G' :
    if litros >= 20 :
      valorPago = (5.57 * litros) * (1 - 0.06)
      print(f'O valor pago pelo cliente foi de {valorPago:.2f}') 
    else : 
      valorPago = (5.57 * litros) * (1 - 0.04)
      print(f'O valor pago pelo cliente foi de {valorPago:.2f}') 

