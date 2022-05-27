from datetime import datetime


def voto(ano):
    atual = datetime.today().year
    idade = atual - ano
    if idade >= 18 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'


num = int(input('Em que ano você nasceu? '))
print(voto(num))
