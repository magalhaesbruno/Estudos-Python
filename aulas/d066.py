n = 0
soma = 0
while True:
    n = int(input('Digite um número ou digite [999] para sair: '))
    if n == 999:
        break
    soma += n
print(soma)