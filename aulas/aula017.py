a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')


valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
    
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei os valores {v}.')