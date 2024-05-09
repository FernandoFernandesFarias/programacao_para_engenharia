d = {"nome": '', "idade": 0, "endereco": '', "telefone": 0}

nome = input('Nome: ')
idade = int(input('Idade: '))
endereco = input('Endereço: ')
tel = int(input('Telefone: '))

d.update({"nome": nome, "idade": idade, "endereco": endereco, "telefone": tel})
print(d)