tupla = (int(input('Type number:')), int(input('Type number:')), int(input('Type number:')), int(input('Type number:')))
print(f'You entenred the values {tupla}')

print(f'The value 9 appears {tupla.count(9)} times')

if 3 in tupla:
    print(f'The value 3 appears in the {tupla.index(3)+1}th position')
else:
    print(f'Does not have the value 3 in any position')
print(f'The amount of numbers divisible by 2 is',end=' ')
for number in tupla:
    if  number%2 == 0:
        print(number,end=' ')
print(' ')

