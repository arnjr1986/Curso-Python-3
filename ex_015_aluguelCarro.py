#Aluguel de carro

car = input('Qual o veículo alugado: ')
d = int(input('Quantidade de dias alugado: '))
vd = float(input('Valor da diária: R$ '))
km = float(input('quantidade de Km percorrido: '))
vkm = float(input('Valor do km percorrido: R$ '))

aluguel = (d*vd)+(km*vkm)

print('O veiculo alugado foi {}\n Por {}dias\nPercorreu {}Kms'.format(car,d,km))
print('O valor da diária é R${}\nO valor do km percorrido é R${}\nO valor total a pagar é: R$ {}'.format(vd,vkm,aluguel))