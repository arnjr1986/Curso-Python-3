"""Ler uma frase e mostrar quantas vezes aparece a letra 'a'
em que posição ela aparece a primeira vez
e em qual posição ela aparece pela ultima vez"""

frase = str(input('Digite uma frase: ')).upper().strip()#Maiusculas e sem espaços
print('A letra *A* aparece {} vezes na frase.'.format(frase.count('A')))#count conta

print('A primeira letra *A* apareceu na posição {}.'.format(frase.find('A')+1))#+1 p/ adequar


print('A última letra *A* apareceu na posição {}.'.format(frase.rfind('A'))+1)#Começa da direita
