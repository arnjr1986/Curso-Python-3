""""Ler dois numeros inteiros e compare-os mostrando:
- O primeiro valor é maior
- O segundo valor é menor
- -Não existe valor maior, os dois são iguais"""

from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('{} é o maior e {} é o menor'. format(n1, n2))
elif n2 > n1:
    print('{} é o Maior e {} é o menor.'.format(n2, n1))
else:
    print('Não existe valor maior, {} é igual a {}'.format(n1, n2))
sleep(2)
print('\nSee you next time')
