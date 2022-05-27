valores = [[], []]
dados = list()
n = 0
for c in range (1,8):
   dados.append(int(input(f'Digite {c}° valor: ')))
for p in dados:
    if p % 2 == 0:
        valores[0].append(p)
    else:
        valores[1].append(p)

print(valores)