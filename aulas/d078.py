lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores: {lista}')
for i, v in enumerate(lista):
    if v == maior:
        print(f'O maior valor digitado foi: {maior} nas posições {i}')
    if v == menor:
        print(f'O menor valor digitado foi: {menor} nas posições {i}')

print(f'O maior digitado foi {maior} nas posições {lista.index(maior)}...{lista.index(maior)}')
print(f'O menor valor digitado foi {menor} nas posições {lista.index(menor)}...')