import os

mesesTemperatura = {}
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
temperaturasAcimaDaMedia = []
mesesTemperaturasAcimaMedia = []
mediaTemperaturas = 0

for mes in meses:
  temperaturas.append(int(input(f'Digite a temperatura do mês de {mes}: ')))

for temperatura in temperaturas:
  mediaTemperaturas += temperatura

mediaTemperaturas = mediaTemperaturas / len(meses)

for temperatura in temperaturas:
  if temperatura > mediaTemperaturas:
    temperaturasAcimaDaMedia.append(temperatura)

for temperatura, mes in zip(temperaturas, meses):
  mesesTemperatura.update({mes: temperatura})

for mesTemperaturaAcimaMedia in mesesTemperatura.items():
  if mesTemperaturaAcimaMedia[1] > mediaTemperaturas:
    mesesTemperaturasAcimaMedia.append(mesTemperaturaAcimaMedia)

os.system('cls' if os.name == 'nt' else 'clear')

print(20 * '-', 'TEMPERATURAS', 20 * '-')
print(temperaturas)
print(20 * '-', 'MESES E SUAS TEMPERATURAS', 20 * '-')
print(mesesTemperatura)
print(f'Média anual: {mediaTemperaturas:.2f}')
print(f'Temperaturas acima da média: {temperaturasAcimaDaMedia}')
print(20 * '-', 'MESES COM TEMPERATURAS ACIMA DA MÉDIA', 20 * '-')
print(mesesTemperaturasAcimaMedia)