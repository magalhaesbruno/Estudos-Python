casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite em quantos anos deseja pagar: '))
meses = anos * 12
base = salario * 0.3
mensal = casa/meses
if mensal > base:
    print('Você não pode comprar esta casa, vai comprometer a sua renda.')
else:
    print('Parabéns, financimaneto aprovado!! as parcelas ficaram no valor de : {:.2f}'.format(mensal))