nome = 'Arnaldo';3
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá, muito prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))


"""nome = input('Nome: ')
print('Prazer em conhecer {}{}{}'.format('\033[4;31;42m', nome, '\033[m'))
"""
