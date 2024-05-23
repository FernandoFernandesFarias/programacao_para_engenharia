compras = {}
total = 0

while True:
  cod = int(input('Código: '))
  produto = input('Produto: ')
  preco = float(input('Preço: '))
  quantidade = int(input('Quantidade: '))
  produtos = []
  produtos.append(produto)
  produtos.append(preco)
  produtos.append(quantidade)
  compras.update({cod: produtos})

  resp = input('Deseja continuar? (S/N): ').upper()
  if resp == 'N':
    break

print(20 * '-')
for cod, produto in compras.items():
  subtotal = compras[cod][1] * compras[cod][2]
  print(f'{produto[0]}: R${subtotal:.2f}')
  total += subtotal

print(f'O total gasto foi de R$ {total:.2f}')
