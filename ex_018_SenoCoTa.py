#Ler ângulo e mostre o valor de seno, cosseno e tangente desse ângulo

from math import radians, cos, sin, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(angulo, cosseno))

tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE {:.2f}'. format(angulo, tangente))
