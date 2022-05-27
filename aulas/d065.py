n = 0
c = ''
lista = []
while c != 'N':
    n = int(input('Digite um número'))
    lista.append(n)
    c = str(input('Quer continuar? [S/N]')).upper()
media = sum(lista) / len(lista)
print('Você digitou {} números e a média foi {}'.format(len(lista), media))
print('O maior valor digitado foi {} e o menor foi {}'.format(max(lista),min(lista)))