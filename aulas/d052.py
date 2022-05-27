cont = 0
div = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        div+= 1
        print(c)
if div == 2:
    print('O número {} foi divisivel {} vezes.'.format(n,div))
    print('Por isso ele é PRIMO')
else:
    print('O número {} foi divisivel {} vezes.'.format(n,div))
    print('Por isso ele não é PRIMO')
