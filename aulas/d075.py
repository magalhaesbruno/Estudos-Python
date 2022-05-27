lista = (int(input('Digite um número: ')), int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: ')))
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor três apareceu na {lista.index(3)+1}° posição ')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
for c in lista:
    if c % 2 == 0:
        print(f'Os valores pares digitados foram {c}')

