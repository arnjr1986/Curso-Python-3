"""Categorias de Natação
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: Sênior
- acima: MASTER"""


#from datetime import .....date ano = date.today().year
idade = int(input('Digite a idade do Atleta: '))

if idade > 0 and idade <= 9:
    print('O Atleta tem {} anos e pertence a categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('O Atleta tem {} anos e pertence a categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('O Atleta tem {} anos e pertence a categoria JUNIOR'.format(idade))
elif idade == 20:
    print('O Atleta tem {} anos e pertence a categoria Sênior'.format(idade))
elif idade > 20:
    print('O Atleta tem {} anos e pertence a categoria MASTER'.format(idade))
else:
    print('A pessoa não tem idade para ser atleta')