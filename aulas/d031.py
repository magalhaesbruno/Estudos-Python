distancia = float(input('Digite a distância da sua viagem: '))
if distancia <= 200:
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('E o preço da sua viagem vai custar: {}R$'.format(distancia * 0.5))
else:
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('E o preço da sua viagem vai custar {}R$'.format(distancia * 0.45))