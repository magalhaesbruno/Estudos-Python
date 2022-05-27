from datetime import date
sexo = str(input('Qual o seu sexo? ')).upper()
atual = date.today().year
nascimento = int(input('Digite a data do seu nascimento:'))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {} '.format(nascimento,idade,atual))
if sexo == 'MASCULINO':
    print('Alistamento Obrigatório')
else:
    print('Sexo Feminino não pode realizar alistamento.')

if idade < 18 and sexo == 'MASCULINO' :
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em: {}'.format(((18 - idade) + atual)))

elif idade > 18 and sexo == 'MASCULINO':
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu alistamento foi em: {}'.format(atual -(idade - 18)))
elif idade == 18 and sexo == 'MASCULINO':
    print('VOCÊ TEM QUE SE ALISTAR IMEDIAMENTE!!')

