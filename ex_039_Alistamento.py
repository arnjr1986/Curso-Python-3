"""LER  O ANO DE NASC. DE UM JOVEM E INFORMAR:
- SE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
- SE É A HORA DE SE ALISTAR
- SE JA PASSOU O TEMPO DE ALISTAMENTO
-MOSTRAR QUANTO TEMPO FALTA OU QUE PASSOU DO PRAZO"""

from datetime import date
nasc = int(input('Digite o ano de Nascimento: '))
alist = int(18)

ano = date.today().year

if ano - nasc == alist:
    print('Você tem {}anos'.format(ano-nasc))
    print('Você deve se alistar este ano')
elif ano - nasc < alist:
    print('Você tem {}anos'.format(ano - nasc))
    print('Você não precisa se alistar ainda faltam {} anos'.format(alist - (ano-nasc)))
elif ano - nasc > alist:
    print('Você tem {}anos'.format(ano - nasc))
    print('Já passou o prazo de alistamento há {} anos '.format((ano-nasc) - alist))
