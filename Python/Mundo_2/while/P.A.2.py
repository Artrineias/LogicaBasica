a = int(input('Primeiro Termo:'))
r = int(input('Razão:'))
pa = a
condição = 10
contador = 0
print('P.A = {}'.format(a),end='')
while (condição!=0):
    pa += r
    condição -= 1
    contador += 1
    print('→{}'.format(pa),end='')
    if condição== 1:
        print('→Fim')
        condição = int(input('Mas quantos termos você quer? '))
        condição += 1
        if condição < 0:
            print('Operação invalida!!!')
            condição = 0