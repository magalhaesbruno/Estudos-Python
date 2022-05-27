p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
termo = p
while c < 10:
    print(termo)
    termo += r
    c +=1

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = p + r * (10-1)
for c in range(p,decimo+1,razão):
    print(c)
