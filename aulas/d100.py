from random import randint
from time import sleep
def sorteia():
    print(f'Sorteando 5 valores da Lista:', end=' ')
    for c in range(0,5):
        a = randint(0, 10)
        lista.append(a)
        print(f'{lista[c]}', end=' ')
        sleep(0.3)
    print()

def somaPar(soma):
    for c in range(0,len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'Somando os valores da lista {lista}, temos {soma}')


lista = list()
a = 0
sorteia()
somaPar(a)
