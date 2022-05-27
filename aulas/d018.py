import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de: {}° tem o seno de: :{:.2f}'.format(angulo,seno))
print('O ângulo de: {}° tem o cosseno de :{:.2f}'.format(angulo,cos))
print('O ângeulo de :{}° tem a tangente de: {:.2f}'.format(angulo,tan))