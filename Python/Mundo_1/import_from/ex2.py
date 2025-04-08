from math import radians, sin, cos, tan

num = float(input('Digite o valor do angulo:'))
radi = radians(num)

print('O angulo digitado foi {:.2f}'.format(num))
print('O seno desse angulo é {:.2f}'.format(sin(radi)))
print('O coso desse angulo é {:.2f}'.format(cos(radi)))
print('A tangente desse angulo é {:.2f}'.format(tan(radi)))
