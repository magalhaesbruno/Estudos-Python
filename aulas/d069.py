idade = 0
sexo =''
print('-==-==--==-==- Cadastre uma Pessoa -==-==--==-==-')
homens = mulheres = maior = 0
continuar = ''
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o Sexo [M/F] :')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Sexo invalido, digite novamente.')
        sexo = str(input('Digite o Sexo [M/F] :')).upper()
    if idade > 18:
        maior +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        mulheres +=1
    continuar = str(input('Deseja Continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 nanos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')