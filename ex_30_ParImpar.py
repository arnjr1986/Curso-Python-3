"""Lê um número inteiro e mostra se é par ou impar"""

n = int(input('Digite um número: '))

if n % 2:
    print('{} é um número impar'.format(n))

else:
    print('{} é um número par'.format(n))

