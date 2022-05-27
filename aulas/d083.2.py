expre = str(input('Digite a sua expressão: '))
lista = []
for c in expre:
    if '(' in c:
        lista.append('(')
    elif ')' in c:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')