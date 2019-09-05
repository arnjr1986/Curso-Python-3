#sortear um aluno entre quatro, para apagar o quadro.
#Ler o nome deles, e escrevendo o nome do escolhido

#from random import choice
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)#retirar random.

print('O escolhido foi {}'.format(escolhido))
