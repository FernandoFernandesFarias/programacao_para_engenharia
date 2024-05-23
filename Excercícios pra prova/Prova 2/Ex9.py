d = {}

nome = input('Nome: ')
idade = int(input('Idade: '))
endereco = input('Endereço: ')
telefone = int(input('Telefone: '))

d.update({'nome': nome, 'idade': idade, 'endereco': endereco, 'telefone': telefone})

print(d)