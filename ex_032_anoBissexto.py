"""Ler se o Ano é Bissexto"""
from datetime import date #Importa modulo de data
ano = int(input('Digite o ano ou 0 se quiser verificar ano atual: '))
if ano == 0:
    ano = date.today().year #chama metodo data atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('O ano {} é Bissexto.'. format(ano))

else:
    print('O ano {} não é Bissexto.'.format(ano))
