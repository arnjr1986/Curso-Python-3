frase = 'Curso em Vídeo Python'
print(frase)

#fatiando
print('Mostra a Posição 3 da string é: ', frase[3])#mostra posição 3 da frase

print('Mostra da Posição 3 até a 13 é: ', frase[3:13])#mostra da posição 3 ate 13 da frase

print('Mostra do inicio ate a posição 13: ', frase[:13])#mostra do inicio ate posição 13

print('Mostra da posição 13 até o fim: ', frase[13:])#mostra da posição 13 até o final

print('Mostra do início até o final, pulando de 2em2: ', frase[0::2])

#ANALISE
print('Mostra quantidade de caracteres da String: ', len(frase))

print('Mostra qtas letras -o- aparecem na string: ', frase.count('o'))

print('Mostra qtas letras -o- aparecem de 0 à 13: ', frase.count('o', 0, 13))

print('Mostra a posição onde aparece deo na string: ', frase.find('deo'))

print('Procura se existe a palavra Android: ', frase.find('Android'))

print('Mostra se existe a palavra Curso na string: ', 'Curso' in frase)

#TRANSFORMAÇÃO
print('Substitui a palavra Python por Android: ', frase.replace('Python','Android'))

print('transforma todas as letras em maiúsculas: ', frase.upper())

print('Transforma todas as letras em minúsculas: ', frase.lower())

print('Apenas a primeira letra maiscula: ', frase.capitalize())


print('As primeiras letras em maiúscula: ', frase.title())

#OUTRO TIPO DE EXEMPLO:
print('Remove os espaços em branco no começo e no fim: ', frase.strip())

print('Remove os espaços em branco à direita: ', frase.rstrip())

print('Remove os espaços em branco à esquerda: ', frase.lstrip())


#DIVISÃO DE STRING
print('Recebe indexação nova, as palavra entram numa lista: ', frase.split())

print('(Junta ou separa as letras): ', ' '.join(frase))

print('Transformando tudo em maiúsculo e verificando qts vzs aparece letra -o-: ', frase.upper().count('O'))

dividido = frase.split()
print('Mostra a segunda letra da palavra da frase: ', dividido[2][3])


#TEXTO EM VARIAS LINHAS
print(""""\nESSE É UM TEXTO EM VARIAS LINHAS ESSE É UM TEXTO EM VARIAS LINHAS 
ESSE É UM TEXTO EM VARIAS LINHAS ESSE É UM TEXTO EM VARIAS LINHAS 
ESSE É UM TEXTO EM VARIAS LINHAS 
""")
