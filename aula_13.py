
#Vai imprimir 'digite um numero' 3 vzs para input
'''for c in range(0, 3):
    n = int(input('digite um numero: '))
print('fim')'''

#imprime 'oi' 5x
'''from time import sleep
for c in range(0, 6):
    print('Oi')
    sleep(1)
print('Fim')'''

''' imprime c(numero de 0 a 5)
from time import sleep
for c in range(0, 6):
    print(c)
    sleep(1)
print('Fim')'''

'''#-1 é a iteração, vai começar no 5 e tirar -1 até chegar no 1
from time import sleep
for c in range(6, 0, -1):
    print(c)
    sleep(1)
print('Fim')'''

'''#vai de 0 até 7 de dois em dois
from time import sleep
for c in range(0, 7, 2):
    print(c)
    sleep(1)
print('Fim')'''

'''#Vai contar de 0 até n(valor inserido)
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c) #contagem
print('Fim')'''

#
'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')'''


'''#pedir valores n dentro do for
for c in range(0, 10):
    n = int(input('digite um numero: '))
print('Fim')'''

s = 0
for c in range(0, 4):
    n = int(input('digite um numero: '))
    s += n
print('A soma de todos os valores foi: {}'.format(s))


