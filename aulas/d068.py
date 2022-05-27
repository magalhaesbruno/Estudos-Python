from random import randint
a = 1
cont = 0
total = 0
while True:
    a = randint(0,11)
    n = int(input('Digite um valor: '))
    p = str(input('Par ou Ímpar [P/I]?')).upper()
    total = a + n
    if total % 2 == 0 and p == 'P':
        print(f'Você jogou {n} e o computador {a}. Total de {total} deu Par')
        print('Você venceu')
        cont += 1
    elif total % 2 == 1 and p == 'I':
        print(f'Você jogou {n} e o computador {a}. Total de {total} deu Ímpar')
        print('Você Venceu')
        cont += 1
    elif total % 2 == 0 and p == 'I':
        print(f'Você jogou {n} e o computador {a}. Total de {total} deu Par')
        print('GAME OVER!! Você Perdeu')
        break
    else:
        print(f'Você jogou {n} e o computador {a}. Total de {total} deu Ímpar')
        print('GAME OVER!! Você Perdeu')
        break

print(f'Você venceu {cont} vezes')