#Tabuada
from time import sleep
num = int(input('Digite um numero para ver sua tabuada: '))

print('='*40)

for c in range(0, 11):
    print('{} x {} = {}' .format(num, c, num*c))
    sleep(1)

print('='*40)
print('Fim')
