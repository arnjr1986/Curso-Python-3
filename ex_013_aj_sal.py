#Ajuste salarial

sal = float(input('Salário: R$ '))
aj = float(input('Informe a % do ajuste salarial: '))

nsal = sal+(sal*aj/100)

print('O salário de R${:.2f}, teve um reajuste de {}%\nO valor salário reajustado é: R$ {}'.format(sal,aj,nsal))

