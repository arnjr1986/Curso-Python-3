#Conversão Cambial

carteira = float(input('Quanto de dinheiro você possui? R$ '))
dolar = float(input('Quanto custa US$ 1 na paridade com BRL: R$ '))

cambio = carteira/dolar

print('Com R$ {:.2f}, você pode comprar US$ {:.2f}.'.format(carteira,cambio))


