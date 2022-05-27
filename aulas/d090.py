escola = {}
escola['nome'] = str(input('Nome: '))
escola['média'] = float(input('Digite a média: '))
if escola['média'] >= 7.0:
    escola['status'] = 'Aprovado!'
else:
    escola['status'] = 'Reprovado!'
for k,v in escola.items():
    print(f'{k} é igual a {v}')