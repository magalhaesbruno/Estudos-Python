from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem: {} anos'.format(idade))
if idade <= 9:
    print('A classificação dele é MIRIM.')
elif idade <= 14:
    print('A classificação dele é: INFANTIL')
elif idade <= 19:
    print('A classificação dele é JÚNIOR:')
elif idade <= 25:
    print('A classificação dele é SÊNIOR.')
else:
    print('A classificação dele é MASTER.')