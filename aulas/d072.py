extenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20:'))
while True:
        if n < 0 or n > 20:
            print('Tente novamente')
            n = int(input('Digite um número entre 0 e 20:' ))
        else:
            break
print(f'Você digitiou o número {extenso[n-1]}')
