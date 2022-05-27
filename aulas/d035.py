p1 = float(input('Primeiro Segmento: '))
p2 = float(input('Segundo Segmento: '))
p3 = float(input('Terceiro Segmento: '))
if  p1 + p2 > p3 and p1 + p3 > p2 and p2 + p3 > p1:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO')