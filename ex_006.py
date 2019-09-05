#Dobro, triplo, raiz Quadrada

n = float(input('Digite um número: '))

d = n*2
t = n*3
r = n**(1/2)

#forma1
print('O valor digitado foi: {}\nSeu dobro é: {}\nSeu Triplo é: {}\nE sua raíz quadrada é: {:.2f}'.format(n,d,t,r))

#forma2
print('O valor digitado foi: {}\nSeu dobro é: {}\nSeu Triplo é: {}\nE sua raíz quadrada é: {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))#pow(n,(1/2)

