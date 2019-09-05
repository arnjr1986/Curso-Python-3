from time import sleep
from random import randint
computador = randint(0, 5)#computador randomiza um numero entre 0 e 5
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...)')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))#jogador um número de 0 a 5
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('ERROUU, eu pensei no {} e não no {}.'.format(computador, jogador))


