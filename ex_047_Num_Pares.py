'''programa que mostra todos os números pare que estão no intervalo entre 1 e 50'''

print('Números Pares de 1 a 50')

'''for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')'''

#maneira economica
for n in range(2,51,2):
    print(n, end=' ')
print('Acabou')
