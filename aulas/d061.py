p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
while cont <= 10:
    print('{}'.format(termo))
    termo = termo + r
    cont +=1
