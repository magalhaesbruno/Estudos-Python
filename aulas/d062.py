p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
n = 0
while cont <= 10:
    print('{}'.format(termo))
    termo = termo + r
    cont +=1
n = int(input('Quantos mais deseja exibir: '))
while cont <= n:
    if n != 0:
        print('{}'.format(termo))
        termo = termo + r
        cont += 1
