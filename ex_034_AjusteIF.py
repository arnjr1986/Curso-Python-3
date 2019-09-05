"""Ler o salário de um funcionário, calcular o valor de seu aumento
-Para salários superiores a R$1250, calcular aumento de 10%
-Para salários inferiores ou iguais, calcular aumento de 15%"""

sal = float(input('Informe o Salário: R$ '))


if sal <= 1250:
    aj1 = (sal * 0.15)
    print('O Valor do reajuste foi de: R$ {:.2f}'.format(aj1))
    print('O Salário reajustado é: R$ {:.2f} '.format(sal+aj1))
else:
    aj2 = (sal * 0.10)
    print('O valor do reajuste foi de: R$ {:.2f}'.format(aj2))
    print('O Salário reajustado é: R$ {:.2f}'.format(sal+aj2))

