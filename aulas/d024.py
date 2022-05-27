cidade = str(input('Em qual cidade você nasceu? ')).strip()
nome = cidade.upper()
print(nome[:5] == 'SANTO')
print('SANTO' in nome)
