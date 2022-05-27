n = 0
cont = 0
tab = 0
while True:
    n = int(input('Digite qual tabuada deseja: '))
    if n < 0:
        print('Programa encerrado.')
        break
    for c in range(0,11):
        tab = n * c
        print(f'{n} x {c} = {tab}')