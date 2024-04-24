nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print('O aluno', nome, 'foi aprovado')
else:
    print('O aluno', nome, 'foi reprovado')


