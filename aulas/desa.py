n = int(input('Digite quanto deseja sacar: R$'))
total = n
cedula = 100
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        print(f'Você irá receber {totced} notas de {cedula} R$')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
print('Dinheiro sacado.')
