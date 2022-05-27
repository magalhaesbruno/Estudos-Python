from time import sleep
def contagem(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        for c in range(a, b+1, c):
            print(f'{c}', end=' ')
            sleep(0.3)
    if b < a:
        for c in range(a, b-1, -c):
            print(f'{c}', end=' ')
            sleep(0.3)

print(f'Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11, 1):
    print(f'{c}', end=' ')
    sleep(0.3)
print()
print(f'Contagem de 10 até 0 de 2 em 2')
print()
for c in range(10, -1, -2):
    print(f'{c}', end=' ')
    sleep(0.3)
print()
print('Agora é sua vez de Personalizar a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
contagem(inicio,fim,passo)