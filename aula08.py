#Modulos / Biblioteca/ import
#import math (importa tudo: ceil(arredonda pra cima), floor(arredonda pra baixo
#trunc(trunca o numero para numero inteiro), pow(exponencial), sqrt, factorial
# from math import sqrt, ceil (vai importar somente sqrt e ceil da biblioteca Math) importação otimizada

import math
#from math import sqrt

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))


