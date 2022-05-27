sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo: [M/F] ')).upper()
    if sexo != 'F' and sexo !='F':
        print('Dados inválidos. Por favor, informe seu sexo:')
print('sexo {} registrado com sucesso'.format(sexo))