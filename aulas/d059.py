opção = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opção != 5:
    print('=-==-=-==-=-==-=-==-=-==-')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opção = int(input('>>>> Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1*n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior número é: {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior número é: {}'.format(n1, n2, n2))
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção > 5:
        print('Opção Inválida, tente novamente.')

print('=-==-=-==-=-==-=-==-=-==-')