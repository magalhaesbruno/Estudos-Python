n = float(input('Qual é o preço do produto? '))
d = n-(5/100*n)
print('O produto custava: {}R$, na promoção com desconto de 5% vai custar: {:.2f}R$'.format(n,d))