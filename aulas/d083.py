lista = []
lista.append(str(input('Digite a expressão: ')))
n1 = 0
n2 = 0
for c in lista:
    for v in c:
        if '(' in v:
            n1 += 1
        elif ')' in v:
            n2 += 1
if n1 == n2:
    print('A sua expressão está certa!')
else:
    print('A sua expressão está errada')
print(lista)
