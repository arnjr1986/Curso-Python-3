"""gerar um numero int random 0 a 5
e pedir pro usuario advinhar qual foi o numero
e dizer se acertou ou errou"""

import random
n = int(input('Digite um numero de 0 à 5: '))

num = random.randint(0, 5)

print('O numero digitado foi: {} e o número escolhido {}.'.format(n, num),'Parabéns' if num == n else 'Errou')

