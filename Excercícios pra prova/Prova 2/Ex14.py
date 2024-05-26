pessoas = {}
menorAltura = 99999999
somaPeso = 0
produtoMaisCaro = None
nomesOrdemAlfabetica = []

for i in range(3):
  nome = input(f'Nome - pessoa {i + 1}: ')
  altura = float(input(f'Altura - pessoa {i + 1}: '))
  peso = float(input(f'Peso - pessoa  {i + 1}: '))
  pessoas[i + 1] = (nome, altura, peso)

for chave, pessoa in pessoas.items():
  if pessoa[1] < menorAltura:
    menorAltura = pessoa[1]
  somaPeso += pessoa[2]
  nomesOrdemAlfabetica.append(pessoa[0])

mediaPeso = somaPeso / (i + 1)

print(pessoas)
print(f'Menor altura: {menorAltura:.2f}')
print(f'Média dos pesos: {mediaPeso:.2f}')
print(f'Nomes em ordem alfabética: {sorted(nomesOrdemAlfabetica)}')

