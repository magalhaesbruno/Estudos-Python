frase = str(input('Digite uma frase: ')).strip()
a = frase[::-1]
if frase == frase[::-1]:
    print('O inverso de {} é {}'.format(frase,a))
    print('A frase digitada é um palíndromo.')
else:
    print('O inverso de {} é {}'.format(frase,a))
    print('A frase digitada não é um palíndromo.')

"""if s == inverso:
    print('A palavra: {] é um palíndromo.'.format(frase))
else:
    print('A palavra {} não é um palíndromo'.format(frase))
print(inverso)"""