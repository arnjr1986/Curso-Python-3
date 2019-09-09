"""Estrutura CONDICIONAL ANINHADA (IF ELIF ELSE)"""

nome = str(input('Qual é o seu nome? ')).strip()

if nome == 'Arnaldo':
    print('Belo nome Sr. {}'.format(nome))
elif nome == 'Pedro' or nome =='João' or nome =='Paulo':
    print('Que nome sem graça...')
elif nome in 'Thiago Juliana Ana Carolina':
    print('Seu nome é popular')
else:
    print('Tenha um bom dia, {}!'.format(nome))

print('Tenha um bom dia, {}!'.format(nome))
