from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
for c in range(1,6):
    dado = randint(1, 6)
    jogadores[f'Jogador{c}'] = dado
print('Valores sorteados:')
ranking = list()
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)
print('-='*30)
for k, v in enumerate(ranking):
    print(f'{k+1}° lugar:  {v[0]} com {v[1]}.')
    sleep(1)
print(ranking)