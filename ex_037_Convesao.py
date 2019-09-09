"""converter numero inteiro para para:
- 1 binario
- 2 octal
- 3 hexadecimal"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para Binário
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))#[2:] começa do terceiro ate o fim
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
