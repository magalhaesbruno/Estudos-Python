n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print('A soma é: {} \n o produto é: {} \n a divisão é: {:.3f}'.format(s, m, d))
print('Divisão inteira: {} \n e potência: {} \n e o resto é:{}'.format(di,e,r))
