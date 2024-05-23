num = int(input('Digite um número: '))

fibonacci = [0, 1]

for i in range(num):
  fibonacci.append(fibonacci[-1] + fibonacci[-2])

fibonacci.remove(fibonacci[-1])
fibonacci.remove(fibonacci[-1])
print(fibonacci)

    
