#Preço , Desconto , valor pós desconto

preco = float(input('Qual o valor do produto?: R$ '))
desc = float(input('Digite a % de desconto: '))

vf = preco-(preco*desc/100)

print('O valor de R${:.2f} com {}% de desconto, sai por R${:.2f}'.format(preco,desc,vf))
