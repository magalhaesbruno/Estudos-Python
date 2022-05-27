from random import randint
matriz = []
cont = tot = 0
print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'-=-=-= Sorteando {n} Jogos -=-=-=')
while cont < n:
    for b in range(1,n):
        while tot < 6:
            a = randint(1, 60)
            if a not in matriz:
                matriz.append(a)
                matriz.sort()
                tot +=1
    print(f'Jogo{cont+1}: {matriz}')
    matriz.clear()
    tot = 0
    cont +=1
print(f'-=-=-= < BOA SORTE! > -=-=-=')
