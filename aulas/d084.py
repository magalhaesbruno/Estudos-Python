cadastro = list()
dados = list()
continuar = ''
atual = 0
mepeso = 0
maiorpeso = menorpeso = 0
cont = 0
while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    cadastro.append(dados[:])
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    dados.clear()
    cont += 1
    if continuar == 'N':
        break
    for p in cadastro:
        if p[1] >= atual:
            atual = p[1]
        elif p[1] < menorpeso or menorpeso == 0:
            menorpeso = p[1]

print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso cadastrado foi: {atual}Kg. Peso de:', end='')
for m in cadastro:
    if atual == m[1]:
        print(f' [{m[0]}] ', end='')
print()
print(f'O menor peso foi {menorpeso}Kg. Peso de:', end='')
for p in cadastro:
    if menorpeso == p[1]:
        print(f'[{p[0]}] ', end='')
