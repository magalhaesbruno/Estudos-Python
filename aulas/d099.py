from time import sleep
def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados.')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('-=' * 20)

maior(2,4,5,6,7,8)
maior(1,2,3,4,5,65,)
