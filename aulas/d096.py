def area(l,c):
    print('Conrole de Terrenos')
    print('-'*20)
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)