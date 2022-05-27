n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
lista =[n1,n2,n3]
lista.sort()
print('O menor número é {}'.format(lista[0]))
print ('O maior número é {}'.format(lista[-1]))





'''n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
#Verificando o menor
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
#Verificando o maior
maior = n1
if n2 > n3 and n2 > n1:
    maior: n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior número é: {}'.format(maior))
print('O menor número é:{}'.format(menor))'''