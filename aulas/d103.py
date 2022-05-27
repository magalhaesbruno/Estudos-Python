def gols(gol='', nome=''):
    if gol == '':
        return f'O jogador {nome} fez 0 gols.'
    if nome == '':
        return f'O jogador <desconhecido> fez {gol}(s) no campeonato.'
    if nome == '' and gol == '':
        return f'O jogador <desconhecido> fez 0 gols no campeonato'

    return f'O jogador {nome} fez {gol}(s) no campeonato.'


jogador = str(input('Nome do jogador: '))
ngols = str(input('Número de Gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
print(gols(ngols, jogador))