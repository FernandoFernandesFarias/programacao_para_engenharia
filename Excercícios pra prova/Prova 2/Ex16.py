d = {}

texto = input('Digite algo: ')

texto = list(texto)

for caracter in texto:
  d[caracter] = texto.count(caracter)

print(d)
