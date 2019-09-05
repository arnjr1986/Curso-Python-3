"""#Mostrar o nome de uma pessoa, o nome com todas letras maiusculas, o nome com letra minusculas
#quantas letras ao todo (sem considerar espaço), quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu Nome Completo: ')).strip()

#Mostrar o nome de uma pessoa
print('1- O nome digitado foi: {}'.format(nome))

#Mostrar o nome com todas letras maiusculas
print('2- Todas as letras Maiúscula: ', nome.upper())
#print('o nome é: {}'.format(nome.upper()))

#Mostrar o nome com todas as letras minúsculas
print('3- Todas as letras Minúsculas: ', nome.lower())
#print('o nome é: {}'.format(nome.lower()))

#Mostrar quantas letras ao todo, (sem considerar espaço)
print('4- Mostrar quantas letras possui, sem espaço: {}'.format(len(nome) - nome.count(' ')))

#Mostrar quantas letras tem o Primeiro nome
#print('O primeiro nome tem: {}letras.'.format(nome.find(' ')))
separa = nome.split()#lista
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))