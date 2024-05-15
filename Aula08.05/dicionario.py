d = {"nome": '', "idade": 0, "endereco": '', "telefone": 0}

nome = input('Nome: ')
idade = int(input('Idade: '))
endereco = input('Endereço: ')
telefone = int(input('Telefone: '))

d.update({"nome": nome, "idade": idade, "endereco": endereco, "telefone": telefone})
print(f'{d["nome"]} tem {d["idade"]} anos, mora na rua {d["endereco"]} e o seu telefone é {d["telefone"]}')