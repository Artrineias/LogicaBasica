print('Para fazer a P.A. é preciso de alguns valores, a Razão e o numero inicial.')
r = int(input('Razão: '))
a = int(input('Numero: '))
base = 0
a_1 = a + r
print('P.A.= {}'.format(a),end='')
while (base < 9):
    print(',{}'.format(a_1),end='')
    a_1 += r
    base += 1

print(" ")
