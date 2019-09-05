"""Analise de Strings
Programa que Lê o nome completo de uma pessoa, mostrando o Primeiro e o Ultimo nome
separadamente"""

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()#split fatia o conteudo separado por espaços

print('Seu primeiro nome é {}.'.format(nome[0]))

print('Seu último nome é {}.'.format(nome[len(nome)-1]))

"""Faz uma lista com conteudo separado por espaço
ex: Nome: jose arnaldo de oliveira junior
[jose, arnaldo, de, oliveira, junior]
   0       1    2       3       4

primeiro da nome da lista é jose[0]
ultimo nome da lista é junior[4], entao se colocar 5-1 vai mostrar o 4
"""