def notas(*num, show=False):
    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = sum(num) / len(num)
    if show == True:
        if dados['média'] >=7:
            dados['situação'] = 'Boa!'
        elif 7 >= dados['média'] and dados['média'] >= 5:
            dados['situação'] = 'Mediana'
        else:
            dados['situação'] = 'Péssima'
    return dados
resp = notas(5.5, 2.5, 3, 9, show=True)
print(resp)