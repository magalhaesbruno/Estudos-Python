n = float(input('Qual é o salário do Funcionário? '))
novo = n + (n*15/100)
print('Um funcionário que ganhava {:.2f}R$, com 15% de aumento, passa a receber {:.2f}R$'.format(n,novo))