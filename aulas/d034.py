salario = float(input('Digite o seu salario atual: R$'))
if  salario <= 1250:
    novo = salario + (0.15 * salario)
    print('Quem ganhava R$:{} passa a ganhar: R${}'.format(salario,novo))
else:
    novo = salario + (0.1 * salario)
    print('Quem ganhava R${} passa a receber R${}'.format(salario,novo))