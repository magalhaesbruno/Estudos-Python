import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1,a2,a3,a4]
print('O aluno escolhido sera: {}.'.format(random.choice(lista)))
random.shuffle(lista)
print('E a ordem para apresentação será: {}.'.format(lista))




""" import random
alu = [input('Primeiro aluno: '), input('Segundo aluno: '), input('Terceiro aluno: '), input('Quarto aluno: ')]
ale = random.choice(alu)
random.shuffle(alu)
print('O aluno escolhido foi: {}'.format(ale))
print('E a  ordem de apresentação será: {}.'.format(alu))"""