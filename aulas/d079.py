"""lista = []
cadastro = ''
while True:
    lista.append(int(input('Digite um número: ')))
    for c in lista:
        if lista.count(c) > 1:
            print('Valor já inserido, o mesmo não será cadastrado')
            lista.remove(c)
        else:
            print('Valor cadastrado com sucesso!')
    cadastro = str(input('Deseja continuar [S/N]?')).upper()
    if cadastro == 'N':
        break
sorted(lista)
print(f'Os valores digitados foram: {lista}')"""

#Ou pode ser feito assim:

números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Valor cadastrado com sucesso!')
    else:
        print('O número não foi cadastrado, pois o mesmo é duplicado.')
    teste    = str(input('Deseja Continuar? [S/N]')).upper()
    if teste == 'N':
        break
sorted(números)
print(f'Os números digitados foram: {números}')