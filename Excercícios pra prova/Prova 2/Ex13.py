produtos = {}
maiorPreco = 0
produtoMaisCaro = None

for i in range(3):
  produto = input(f'Digite o nome do produto {i + 1}: ')
  descricao = input(f'Digite a descrição do produto {i + 1}: ')
  preco = float(input(f'Digite o preço do produto {i + 1}: '))
  produtos[i + 1] = (produto, descricao, preco)

for chave, valor in produtos.items():
  if valor[2] > maiorPreco:
    maiorPreco = valor[2]
    produtoMaisCaro = valor

print(f"Produto mais caro: {produtoMaisCaro}")
print("Lista de produtos:")
for chave, valor in produtos.items():
  print(valor)
