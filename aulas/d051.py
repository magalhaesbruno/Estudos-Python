p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = p + r * (10-1)
for c in range(p,decimo + 1,r):# pode-se usar váriaveis também, vai começar do valor que a váriavel p recebeu, vai até o valor da variavel decimo e vai pulando os valores de acordo a váriasvel r
    print(' {} '.format(c),end=' ')
print('Acabou')

'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = int(input('Termo: '))
décimo = primeiro + razão * (termo - 1)
for cont in range(primeiro,décimo + 1,razão):
    print(cont)'''