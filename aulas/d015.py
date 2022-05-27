dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos Kilometros foi percorrido? '))
pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de: {:.2f}R$'.format(pagar))