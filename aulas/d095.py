cadastro = dict()
gols = list()
jogadores = list()
total = 0
continuar = ''
while True:
    gols.clear()
    cadastro.clear()
    cadastro['nome'] = str(input('Digite o nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou?'))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}?')))
        total = sum(gols)
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper()
        if continuar in 'NS':
            break
        print('Digite somente S ou N')
    cadastro['gols'] = (gols[:])
    cadastro['total'] = total
    jogadores.append(cadastro.copy())
    if continuar == 'N':
        break
print('-=' * 30)
print(f'cod nome gols total')
for k, v in enumerate(jogadores):
    print(f'{k:>4} {v["nome"]} {v["gols"]} {v["total"]}')
while True:
    a = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if a == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[a]["nome"]}')
    for i, g in enumerate(jogadores[a]['gols']):
        print(f'No jogo {i+1} fez {g} gols')
print(jogadores)
print(jogadores[0]['nome'])
print(jogadores[0]['gols'])


