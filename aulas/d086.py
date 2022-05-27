matriz = [[], [], []]
n = 0
for c in range(0,9):
    if len(matriz[0]) < 3:
        matriz[0].append(int(input(f'Digite um valor :')))
    elif len(matriz[1]) < 3:
        matriz[1].append(int(input('Digite um valor: ')))
    elif len(matriz[2]) < 3:
        matriz[2].append(int(input('Digite um valor')))
for c in range(0,3):
    for b in range(0,3):
        print(f'[{matriz[c][b]:^5}]', end='')
    print()

print(f'[  {matriz[0][0]}  ] ', end='')
print(f'[  {matriz[0][1]}  ] ', end='')
print(f'[  {matriz[0][2]}  ] ')

print(f'[  {matriz[1][0]}  ] ', end='')
print(f'[  {matriz[1][2]}  ] ', end='')
print(f'[  {matriz[1][2]}  ] ')

print(f'[  {matriz[2][0]}  ] ', end='')
print(f'[  {matriz[2][1]}  ] ', end='')
print(f'[  {matriz[2][2]}  ] ')