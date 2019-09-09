'''programa que leia o primeiro termo e a razão de uma Progressão Aritmetica
mostre os 10 primeiros termos dessa P.A'''

term = int(input('Insira o Primeiro Termo da P.A: '))
raz = int(input('Insira a Razão da P.A: '))
decimo = term + (10-1) * raz

for c in range(term, decimo + raz, raz):
    print(c, end=' ')
