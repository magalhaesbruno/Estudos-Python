lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar? [S/N] ')).upper()
    if c == 'N':
        print(f'Você digitou {len(lista)} elementos')
        print('A sua lista em ordem decrescente são:', end='')
        lista.sort(reverse=True)
        print(lista)
        if 5 in lista:
            print('O valor 5 faz parte da lista')
        else:
            print('O valor 5 não foi encotrado')
        break