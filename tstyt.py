x = input('Digite um número: ')
print(f'Ele é alfa? {x.isalpha()}'
      f'\nEle é número? {x.isalnum()}'
      f'\nEle é decimal? {x.isdecimal()}'
      f'\nEstilo do seu digito é: '
      f'{type(x)}')
