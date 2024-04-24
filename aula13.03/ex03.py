a = int(input("Digite um número qualquer: "))
b = int(input("Digite um número DIFERENTE de 0: "))

try :
    print (a / b)
except ZeroDivisionError :
    print ('Divisão por zero - inválida')