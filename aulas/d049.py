n = int(input('Digite um número para ver sua tabuada: '))
print('{:=^20}'.format('='))
for c in range(0,11):
    print('{} x {} = {}'.format(n,c,n*c))
print('{:=^20}'.format('='))