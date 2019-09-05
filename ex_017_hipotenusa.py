#cateto oposto, cateto adjacente de um triangulo retângulo
#Mostre o comprimento da hipotenusa (hipotenusa = a soma do quadrado dos catetos

import math
ca = int(input('Insira o valor do Cateto Adjacente: '))
co = int(input('Insira o valor do cateto oposto: '))

'''h = (ca**2 + co**2) ** (1 / 2)


print('A hipotenusa é: {}'.format(h))'''

h = math.hypot(ca, co)

print('A hipotenusa é {:.2f}'.format(h))





