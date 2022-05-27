import random
print('SUAS OPÇÕES: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
opção = int(input('Qual é a sua jogada? '))
print('JO')
print('KEN')
print('PO')
print('-=' * 11)
lista = ['PEDRA','TESOURA','PAPEL']
lista1 = ['PEDRA','TESOURA','PAPEL']
print('Jogador escolheu: {}'.format(lista1[opção]))
pc = random.choice(lista)
print('Computador jogou {}'.format(pc))
print('-=' * 11)
if pc == 'TESOURA' and lista1[opção] == 'TESOURA':
    print('EMPATE')
if pc == 'TESOURA' and lista1[opção] == 'PAPEL':
    print('COMPUTADOR VENCE')
if pc == 'TESOURA' and lista1[opção] == 'PEDRA':
    print('VOCÊ VENCEU')
if pc == 'PAPEL' and lista1[opção] == 'TESOURA':
    print('VOCÊ VENCEU')
if pc == 'PAPEL' and lista1[opção] == 'PAPEL':
    print('EMPATE')
if pc == 'PAPEL' and lista1[opção] == 'PEDRA':
    print('COMPUTADOR VENCEU')
if pc == 'PEDRA' and lista1[opção] == 'TESOURA':
    print('COMPUTADOR VENCEU')
if pc == 'PEDRA' and lista1[opção] == 'PAPEL':
    print('VOCÊ VENCE')
if pc == 'PEDRA' and lista1[opção] == 'PEDRA':
    print('EMPATE')
