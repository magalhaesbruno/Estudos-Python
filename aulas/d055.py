lista = []
for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa'.format(c)))
    lista.append(peso)
print('O maior peso lido foi de {}Kg '.format(max(lista)))
print('O menor peso lido foi de {}Kg'.format(min(lista)))
