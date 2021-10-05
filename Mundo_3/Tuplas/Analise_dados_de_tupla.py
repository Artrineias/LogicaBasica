lista = [' ',' ',' ',' ']
for count in range(0,4):
    lista[count] = int(input('Type number:'))

tupla = (lista[0], lista[1], lista[2], lista[3])
print(f'You entenred the values {tupla}')

nine = 0

for count in range(0,4):
    if tupla[count] == 9:
        nine += 1
    
print(f'The value 9 appears {nine} times')

a = 0
for count in range(0,4):
    if tupla[count] == 3:
        a += 1
if a == 1:
    print(f'The value 3 appears in the {tupla.index(3)+1}th position')
else:
    print(f'Does not have the value 3 in any position')

resto = 0

for count in range(0,4):
    division = tupla[count]%2
    if division == 0:
        resto += 1

print(f'The amount of numbers divisible by 2 is {resto}')
