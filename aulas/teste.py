n = int(input('Digite um valor para saber seu fatorial: '))
d = n
soma = 1
for c in range(n, 1, -1):
    soma *= d
    d -= 1
    print(soma)

n2 = int(input('Digite um valor para saber seu fatorial: '))
fatorial = 1

c = n2
while c > 0:
    fatorial *= c
    c -= 1
    print(fatorial)