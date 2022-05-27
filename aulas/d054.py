from datetime import date
data = date.today().year
novo = 0
velho = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    if data - nasc < 18:
            novo += 1
    if data - nasc > 18:
            velho +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(velho))
print('Ao todo tivemos {} pessoas menores de idade'.format(novo))