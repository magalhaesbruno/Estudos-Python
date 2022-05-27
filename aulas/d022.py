nome = str(input('Digite o nome Completo: ')).strip()
print('Este é o seu nome completo: {}'.format(nome))
print('Este é o seu nome completo todo em maisculo: {}'.format(nome.upper()))
print('Este é o seu nome completo todo em minuscula: {}'.format(nome.lower()))
#print('O seu primeiro nome tem: {} letras'.format(nome.find(' ')))
nome = nome.split()
print('O seu primeiro nome tem: {} letras'.format(len(nome[0])))
nome = ''.join(nome)
print('O seu nome completo possui: {} letras'.format(len(nome)))


