print('{:=^40}'.format('LOJAS BRUNO'))
total = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no carão')
print('[ 4 ] 3x ou mais no cartão')
op = int(input('Qual a opção?'))
if 4 > op < 0:
    print('Opções inválidas, tente novamente.')
elif op == 1:
    final = total - (total * 0.1)
    print('Sua compra de: {}R$ vai custar: {}R$ no final.'.format(total,final))
elif op == 2:
    final = total - (total * 0.05)
    print('Sua compra de: {}R$ vai custar: {}R$ no final.'.format(total,final))
elif op == 3:
    parcelas = total/2
    print('Sua compra será parcela em 2x de {}R$ sem juros'.format(parcelas))
elif op == 4:
    final = total + (total * 0.2)
    parcelas = int(input('Digite o número de parcelas: '))
    parcelado = final / parcelas
    print('Sua compra sera parcelada em: {}x com JUROS'.format(parcelado))
    print('Sua compra de: {}R$ vai custar {}R$ no final'.format(total,final))
