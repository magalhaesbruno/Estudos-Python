lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    s = str(input('Deseja continuar? [S/N] ')).upper()
    lista.append(n)
    if s == 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
