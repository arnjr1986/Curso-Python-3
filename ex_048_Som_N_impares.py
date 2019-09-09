'''Programa que soma todos os numeros impares multiplos de tres
e que se encontram no intervalo de 1 até 500'''

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        cont = cont + 1 #contador
        soma = soma + c #acumulador


print('\n A soma dos {} valores é: {}'.format(cont, soma))
