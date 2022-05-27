def fatorial(num,show=False):
    """
    =>Calcula um fatorial de um número:
    :param num: número a ser calculado
    :param show: mostrar ou não  a conta
    :return: o vcalor do Fatorial de um número num
    """
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c,end='')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ',end='')
        f *= c
    return f

#Programa Principal
f = int(input('Digite o número que deseja o fatorial; '))
help(fatorial)