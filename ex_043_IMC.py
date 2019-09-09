"""Calcular IMC
- abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 a 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

peso = float(input('Peso: (Kg)'))
altura = float(input('Altura (m): '))

imc = peso / (altura**2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso ideal')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

