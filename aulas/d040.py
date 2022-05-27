n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1+n2)/2
if 7 > media > 5:
    print('Você está de recuperação!!')
elif media < 5:
    print('Você foi reprovado!')
elif media >= 7:
    print('Você está aprovado')