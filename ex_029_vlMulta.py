"""Ler veloc de um carro
Se passar de 80km/h mostrar que foi multado
mostrar multa de 7 reais por km excedido"""

vel = float(input('Digite a velocidade do veículo: '))

vm = 80
m = 7

if vel > 80:
   multa = (vel - vm) * m
   print('Você excedeu o limite de Velocidade! Multa {}'. format(multa))

else:
  print('Você não foi multado, dirigiu muito bem')
