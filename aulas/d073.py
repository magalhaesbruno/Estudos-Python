times = ('Corinthias', 'Santos', 'América-MG', 'Bragantino',
         'São Paulo', 'Atlético-MG', 'Botafogo', 'Internacional',
         'Coritiba', 'Avaí', 'Cuiabá', 'Athletico-PR',
         'Palmeiras', 'Flamengo', 'Fluminense','Goiás', ''
        'Ceará SC', 'Juventude', 'Atlético-GO', 'Fortaleza')

print('-='*15)
print(f'Os primeiros colocados são {times[0:5]}')
print('-='*15)
print(f'Os últimos colocado são {times[-4:]}')
print('-='*15)
print(f'Lista de times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'Em que posição está o Santos? {times.index("Santos")+1}° posição')
print('-='*15)

