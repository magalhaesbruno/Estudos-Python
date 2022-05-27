cadastro = {}
lista = list()
mediaidade = idade = sexo = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F]')).upper()
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M OU F.')
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro.copy())
    cadastro.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper()
        if continuar in 'SN':
            break
        print('ERRO!Responda apenas S ou N')
    if continuar == 'N':
        break
print('-=' * 30)
for c in lista:
    idade += c['idade']
    mediaidade = idade/len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {mediaidade:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for b in lista:
    if b['sexo'] == 'F':
        print(f'{b["nome"]}', end='')
print()
print('D) A lista de pessoas que estão acima da média é: ')
for d in lista:
    if d['idade'] > mediaidade:
        print(f'nome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]}')