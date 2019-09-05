"""Pergunte a distância da viagem km
calcular o peço da passagem, R$ 0.50 por até 200km
e R$ 0.45 acima de 200km"""

dist = float(input('Qual a distância da viagem em KM?: '))

vc = 0.5
vl = 0.45

if dist >= 200:
    vf = dist*vl
    print('Sua viagem custará R$ {}'.format(vf))

else:
    vf = dist*vc
    print('Sua viagem custará R$ {}'.format(vf))
