frase = input('Digite uma frase: ')

palavraAntiga = input('Digite uma palavra contida na frase acima: ')

while not palavraAntiga in frase :
  print('A palavra não foi encontrada')
  palavraAntiga = input('Digite uma palavra contida na frase acima: ')

palavraNova = input('Digite a nova palavra: ')

fraseNova = frase.replace(palavraAntiga, palavraNova)

print(frase)
print(fraseNova)