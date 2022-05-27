alunos = []
cadastro = list()
media = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Digite a nota 1: ')))
    cadastro.append(float(input('Digite a nota 2: ')))
    media = (cadastro[1] + cadastro[2]) /2
    cadastro.append(media)
    alunos.append(cadastro[:])
    cadastro.clear()
    c = str(input('Deseja continuar? [S/N]')).upper()
    if c == 'N':
        break
print('-'*20)
print(f'{"N°.":4<}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for d, b in enumerate(alunos):
    print(f'{d :<4}{b[0] :<10}{b[3] :>8.1f}')
while True:
   notas =  int(input('Mostrar notas de qual aluno? (999 interrompe): '))
   print(f'As notas de {alunos[notas][0]} são: {alunos[notas][1], alunos[notas][2]}')
   if notas == 999:
       break


