matriz = [[0,0,0], [0,0,0], [0,0,0]]
par= terceira = maior  = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [ {l}, {c} ]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{ matriz[l][c]:^5} ]',end='')
    print()
for c in matriz:
   for b in c:
       if b % 2 == 0:
           par += b
for l in range(0,3):
    terceira += matriz[l][2]
for l in range(0,3):
    if matriz[1][l] > maior:
        maior = matriz[1][l]
print(f'A soma dos valores pares: {par}')
print(f'A soma dos valores da terceira colukna é: {terceira}')
print(f'O maior valor da segunda linha é: {maior}')