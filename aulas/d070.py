p = continuar = nome = ''
preço = barato = caro = total = 0
while True:
    p = str(input('Nome do Produto: ')).upper().strip()
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        caro += 1
    if preço < barato or barato == 0:
        barato = preço
        nome = p
    continuar = str(input('Deseja continuar? [S/N]? ')).upper().strip()
    if continuar == 'N':
        break
print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${barato:.2f}')