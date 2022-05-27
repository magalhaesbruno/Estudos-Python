
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c))
    f *= c #F começa valendo 1, e vai ser então: F = 1 * 6, após executar o contador vai reduzir 1 do C e vai repetir, F = 6 * 5, F = 30 * 4
    c -= 1 #O C começa com o valor digitado pois C = N, e no final , C = C - 1 - C = 6 - 1, C = 5 - 1 , C = 4 -1
print('O fatorial de {} é {}'.format(n,f))

nu = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = 1

for b in range(nu,0,-1):
    print('{}'.format(b))
    fatorial = b * fatorial
print(fatorial)