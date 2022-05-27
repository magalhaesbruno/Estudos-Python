nome = str(input('Qual é o seu nome completo? ')).strip().upper().split()

print('O seu nome tem Silva? {}'.format('SILVA' in nome))