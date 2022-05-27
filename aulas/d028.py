import random
n1 = int(input('Digite um número de 0 a 5: '))
n2 = random.randint(0,5)
if n1 >= 5:
    print('Programa encerrado, número digitado maior que 5')
else :
    if n1 == n2:
        print('Você venceu!')
    else:
        print('Você perdeu!')



