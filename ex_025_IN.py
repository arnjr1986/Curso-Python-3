#Ler nome de uma pessoa e dizer se ela tem SILVA no nome

nome = str(input('Digite o nome completo:')).strip()

print('Possui nome Silva no nome: ', 'Silva' in nome.upper())

