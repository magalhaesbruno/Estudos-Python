saque = int(input('Digite o valor a ser sacado: R$'))
total = saque
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        print(f'O total de {totcedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula =1
        totcedula = 0
        if total == 0:
            break
