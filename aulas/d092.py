from datetime import datetime
cadastro = {}
atual = datetime.today().year
cadastro['nome'] = str(input('Digite o nome: '))
cadastro['Nascimento:'] = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = atual - cadastro['Nascimento:']
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
    cadastro['ctps'] = ctps
    cadastro['contrato'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Digite o salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contrato'] + 35) - datetime.now().year)
for k,v in cadastro.items():
    print(f'- {k} tem o valor {v}')
