def validar_numero():
  while True:
      try:
          num = int(input("Digite um número entre 1 e 10: "))
          if 1 <= num <= 10:
              return num
          else:
              print("Por favor, digite um número entre 1 e 10.")
      except ValueError:
          print("Por favor, digite um número válido.")

num_valido = validar_numero()

for i in range(1, 11):
    print(f'{num_valido} * {i} = {num_valido * i}')