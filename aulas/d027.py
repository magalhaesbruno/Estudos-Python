nome = str(input('Digite o seu nome completo: ')).strip().split()
primeiro = nome[0]
ultimo = nome.pop()
print('O primeiro nome é: {} e o último nome é : {}'.format(primeiro,ultimo))

n = str(input('Digite o seu nome completo: ')).strip().split()
print('O primeiro nome é: {} e o último nome é : {}'.format(n[0],n[-1]))

"""No segundo print ao utilizar n[len(n) -1] , quer dizer que vai ser o último index da lista, pois o len vai contar a 
quantidade de palavras que existem dentro da lista e vai reduzir -1, porque mesmo tendo 4 palavras por exemplo a lista
começa no index 0, por exemplo: Maria Silva Oliveira tem 3 palavras mas, dentro do array o último nome ocupou o index 2
então o n[len(n) -1] vai contar a quantidade de palvras que vai ser 3 - 1 que vai ser igual a 2, que será o index onde vai
estar o último nome."""

"""Pode se usar também nome[-1] pois assim iria começar a contagem do último item da lista"""