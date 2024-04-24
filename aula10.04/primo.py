def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input('Digite um número: '))
resultado = primo(numero)

if resultado:
    print('É primo')
else:
    print('Não é primo')

# i = 1 
# div = 0 

# n = int(input('Digite um número: '))

# while i <= n:
#   if n % i == 0:
#     div += 1
#   i += 1

# if div > 2 or n == 1:
#     print('Não é primo')
# else: 
#    print('É primo')
