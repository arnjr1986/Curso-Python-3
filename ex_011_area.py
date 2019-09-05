#Area e qtd de tinta a ser gasta

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
tinta = area/2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg,alt,area))
print('\nUma lata de tinta rende 2m²')
print('Você precisará de {}L de tinta.'.format(tinta))
