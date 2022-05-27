from time import sleep
def ajuda():
    print('~')
    print('SISTEMA DE AJUDA PyHELP')
    print('~')
    n = 'fim'
    while True:
        suporte = str(input('Função ou Biblioteca?'))
        if suporte != 'fim':
            print('~' * len(suporte))
            print(f'Acessando o comando {suporte}')
            print('~' * len(suporte))
            sleep(1)
            help(suporte)
        else:
            break


ajuda()