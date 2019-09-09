"""Financiamento bancário compra de imóvel
o valor do imovel
o valor do salário
quantidade de anos para pagar
não pode comprometer 30% do salário"""

vl_imovel = float(input('Digite o valor do Imóvel: R$ '))
vl_salario = float(input('Digite o valor do Salário: R$ '))
qt_anos = int(input('Digite em Quantos anos: '))

vl_pres = vl_imovel / (qt_anos*12)

print('Para pagar uma casa de R${:.2f} em {}anos, a prestação sera de {:.2f}'.format(vl_imovel, qt_anos, vl_pres))


print('O valor da parcela é R${:.2f}'.format(vl_pres))

if vl_pres > (vl_salario *0.30):
    print('Você não pode financiar o valor R${}, sua renda é incompatível'.format(vl_imovel))