n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi: {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim! Estude MAIS!')

# print('Parabéns' if m <=6 else 'ESTUDE MAIS!')