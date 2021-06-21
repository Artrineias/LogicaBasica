from math import pow, sqrt

ca = float(input('Digite o cateto adjasente: '))
co = float(input('Digite o cateto oposto: '))

h = sqrt(pow(ca, 2) + pow(co, 2))

print('A hipotenusa desse triangulo é {}'.format(h))
