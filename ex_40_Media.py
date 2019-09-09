"""Ler notas, calcular media
-abaixo de 5.0 REPROVADO
-entre 5.0 e 6.9 RECUPERAÇÃO
-media 7 ou superior aprovado"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media < 5:
    print('Aluno com média {}, está REPROVADO'.format(media))
elif 5 <= media <= 6.9:
    print('Aluno com média {} e está de RECUPERAÇÃO'.format(media))
else:
    print('Aluno com nota {}, APROVADO!'.format(media))