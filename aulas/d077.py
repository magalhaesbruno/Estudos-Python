lista = ('APRENDER','PROGRAMAR', 'LINGUAGEM')
for palavras in lista : # Aqui a variavel palavras percorre por cada palavra da lista
    print(f'\nNa palavra {palavras} temos as vogais: ', end='')
    for vogal in palavras: # aqui a variavel vogal percorre por cada palavra, porém, cada palavra  é uma lista e com isso percorre uma a uma, exemplo: (A-P-R-E-N-D-E-R)
        if vogal.lower() in 'aeiou': #ou seja, em vez de buscar palavra a palvra como na lista acima, a palvra vira uma própria lista.
            print(vogal,end=' ')