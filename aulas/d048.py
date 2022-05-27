soma = 0
c = 0
for cont in range(1, 501, 2): #para contador dentro do alcance de 1 até 501,saltando de 2 em para pegar somente os números ímpares faça
    if cont % 3 == 0:# Se contador dividido por 3 for igual a resto 0 então ele é ímpar
        soma += cont # soma vai receber os números de contadores somando entre eles, exemplo : vai receber 3, depois 3 + 9, depois 3 + 9 = 12 + 15 = 27
        c += 1
print('A soma de todos os {} valores solicitados é: {}'.format(c,soma))