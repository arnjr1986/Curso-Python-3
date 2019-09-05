from time import sleep
distancia = float(input('Qual a distância? Km '))
print('Você fará uma viagem de {}kms'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print('=='*5, 'Calculando o valor da Passagem', '=='*5)
sleep(3)
print('O valor da passagem custará R${}'.format(preço))

