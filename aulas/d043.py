peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura?'))
imc = peso/(altura*altura)
print('O IMC dessa pessoa é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 25 > imc > 18.5:
    print('Parabéns, você está no peso ideal!!')
elif 30 > imc >= 25:
    print('Você está com sobrepeso.')
elif 40 > imc >= 30:
    print('Você está com obesidade')
elif imc > 40:
    print('ATENÇÃO VOCÊ ESTÁ COM OBESIDADE MÓRBIDA, PROCURE AJUDA.')
