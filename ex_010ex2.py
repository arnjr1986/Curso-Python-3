n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))

m = (n1+n2)/2

print('Sua média foi {} você está {}'.format(m, 'Aprovado' if m >= 6 else 'Reprovado'))
