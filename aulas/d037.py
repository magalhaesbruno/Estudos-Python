import math
num = int(input('Digite um número inteiro: '))

print('Escolha uma base para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha >= 4 and escolha == 0:
    print('Escolha errada, tente novamente.')
elif escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)))