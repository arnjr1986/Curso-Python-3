"""Gerenciador de Pagamento: Preço Normal e condição de Pagamento
- à vista dinheiro/cheque: 10% desconto
- à vista Cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format(' LOJA ARNALDO '))#Fazer centralizar e separar com =
produto = float(input('Valor do Produto R$ '))

print('''Forma de pagamento: 
[1] à vista dinheiro/cheque 
[2] à vista no Cartão
[3] Em até 2x no Cartão
[4] 3x ou mais no Cartão''')

formPag = int(input('Escolha a forma de Pagamento: '))

din = produto - (produto * 0.10)
cartao = produto - (produto * 0.05)
parc2 = produto/2
parc3 = produto + (produto * 0.2)

if formPag == 1:
    print('O valor do produto R${} na forma de pagamento escolhida fica: R${:.2f}'.format(produto, din))

elif formPag == 2:
    print('O valor do produto R${} na forma de pagamento escolhida fica: R${:.2f}'.format(produto, cartao))

elif formPag == 3:
    print('O produto de R${} na forma de pagamento escolhida fica: 2x R${:.2f} SEM JUROS'.format(produto, parc2))

elif formPag == 4:
    totalparc = int(input('Quantas Parcelas? '))
    parcela = parc3 / totalparc
    print('Sua compra de R${}, parcelada com juros de 20% fica em {}x R${:.2f}'.format(produto, totalparc, parcela))
    print('O valor final será de {}'.format(parc3))

else:
    print('Forma de pagamento não reconhecida')
