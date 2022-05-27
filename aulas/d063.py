n = int(input('Quantos termos você deseja? '))
c = 0
a = 0
b = 1
d = 0
while d < n:
    a = b
    b = c
    d += 1
    c = a + b
    print(c)