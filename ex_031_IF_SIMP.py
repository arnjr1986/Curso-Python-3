from time import sleep
distancia = float(input('Qual a distância? Km '))
print('Você fará uma viagem de {}kms'.format(distancia))

preço = distancia*0.5 if distancia <= 200 else distancia * 0.45 #IF SIMPLIFICADO

print('=='*5, 'Calculando o valor da Passagem', '=='*5)
sleep(3)
print('O valor da passagem custará R${}'.format(preço))

