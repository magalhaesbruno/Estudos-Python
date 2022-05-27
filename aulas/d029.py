velocidade = float(input('Digite a sua velocidade atual: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia! Dirija sempre com segurança')
else:
    print('MULTADO! Você excedeu o limite permitido de velocidade que é de 80Km/h')
    print('Você deve pagar uma multa de {}R$'.format(multa))
    print('Tenha um bom dia! Dirija sempre com segurança')