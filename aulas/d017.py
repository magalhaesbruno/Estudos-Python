import math
ca = float(input('Digite o valor do Cateto Adjascente: '))
co = float(input('Digite o valor do Cateto Oposto: '))
hyp = math.hypot(ca,co)
print('O comprimento da hiponetusa é: {:.2f}'.format(hyp))