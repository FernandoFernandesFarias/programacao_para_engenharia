numeros = []
numerosCopia = []

for i in range(1, 5):
    numeros.append(int(input(f'Digite o número {i}: ')))

print("Lista original:", numeros)

del(numeros[2])

print("Lista após remoção do terceiro elemento:", sorted(numeros, reverse=True))

for num in numeros:
    numerosCopia.append(num)

print("Cópia da lista:", numerosCopia)

numerosCopia.append(int(input('Digite um número para adicionar: ')))
print("Lista com o número adicionado:", numerosCopia)
