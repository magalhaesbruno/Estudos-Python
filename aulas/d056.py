cont = 0
velho = 0
nomevelho = ''
somaidade = 0
mediaidade = 0
for c in range(1,5):
    print('--------- {}° Pessoa ---------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if idade > velho and sexo == 'M':
        nomevelho = nome
        velho = idade
    if idade < 20 and sexo =='F':
        cont += 1
mediaidade = somaidade/4
print('A media das idades é: {}'.format(mediaidade))
print('O homem mais velho tem {} e seu nome é: {}'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))



"""""
cont = 0
nomes = []
idades = []
sexos = []
posi = 0
nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    if idade < 20 and sexo =='F':
        cont += 1
print('A média de idade do grupo é {}'.format(sum(idades) / len(idades)))
posi = idades.index(max(idades))
print('O homem mais velho tem {} e se chama {}'.format(max(idades), nomes[posi]))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))"""