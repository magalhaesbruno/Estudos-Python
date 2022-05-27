larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('A sua parede tem as seguintes dimensões: {}m de largura e {}m de altura'.format(larg,alt))
print('A sua parede tem {}m² e serão necessários {}l de tinta.'.format(area,tinta))