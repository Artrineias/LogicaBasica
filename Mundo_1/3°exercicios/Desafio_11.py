cels = float(input('Digite o valor da temperatura em C° '))

far = cels * 9 / 5 + 32
kel = cels + 273.15

print('Os valores convertidos pra as outras temperatura é :')
print('F° {}'.format(far))
print('K° {}'.format(kel))
