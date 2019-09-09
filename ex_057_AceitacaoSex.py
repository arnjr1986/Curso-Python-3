'''Programa que leia o sexo de uma pessoa
mas so aceita os valores 'M' ou 'F'
caso esteja errado peça novamente
até ter um valor correto'''

sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Informe seu Sexo com [M ou F]: ')).strip().upper()[0]

print('Sexo {} cadastrado com sucesso!'.format(sexo))


