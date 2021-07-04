cels = float(input('Enter the temperature value in C° '))

far = cels * 9 / 5 + 32
kel = cels + 273.15

print('The values converted to the other temperatures is :')
print('F° {}'.format(far))
print('K° {}'.format(kel))
