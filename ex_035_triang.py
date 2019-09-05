"""Ler 3 valores de 3 retas e dizer se elas podem ou não formar um triângulo"""
print('=='*20)
print('Analisador de Triângulo')
print('=='*20)
r1 = float(input('valor 1: '))
r2 = float(input('valor 2: '))
r3 = float(input('valor 3: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triângulo')

else:
    print('Não é um triângulo')
