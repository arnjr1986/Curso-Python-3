nome = str(input('Digite seu nome: ')).strip().lower()
if nome == 'arnaldo':
    print('Olá Arn você é um super usuário!!!')
    print('Que bom que voltou!')
else:
    print('Você é um usuário comum')
    print('Boa tarde, {}.'.format(nome.capitalize()))

