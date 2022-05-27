jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c} ? ')))
    total += gols[c]
jogador['gols'] = gols
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'Na partida {k}, fez {v} gols.')
print(f'Foi um total {total} gols.')

