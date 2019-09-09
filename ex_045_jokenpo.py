"""Criar jogo JO KEN PO"""

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual a sua escolha? '))
print('-='*30)
print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO')
sleep(1)

print('O computador escolheu {}.'.format(itens[computador]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('-='*30)

if computador == 0: #computador jogou pedra

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
       print('Jogador Venceu')

    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada inválida')

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador Venceu!')

    elif jogador == 1:
        print('Empate!')

    elif jogador == 2:
        print('Jogador Venceu!')

    else:
        print('Jogada inválida')



elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador Venceu!')

    elif jogador == 1:
        print('Computador Venceu!')

    elif jogador == 2:
        print('Empate!')

    else:
        print('Jogada inválida')
