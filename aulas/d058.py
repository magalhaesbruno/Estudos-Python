import random
n1 = random.randint(0, 10)
n2 = -1
cont = 0
print('Sou seu computador... Acabei de pensar em um número entre 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
while n2 != n1:
    n2 = int(input('Qual será seu palpite? '))
    if n2 > n1 and n2 != n1:
        print('Menos...Tente mais uma vez')
        cont +=1
    if n2 < n1 and n2 != n1:
        print('Mais...Tente mais uma vez.')
        cont +=1
print('Acertou com {} tentativas.'.format(cont))

