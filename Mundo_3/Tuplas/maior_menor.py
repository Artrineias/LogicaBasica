from random import randrange
a = [' ',' ',' ',' ',' ']
for count in range(0,5):
    a[count] = (randrange(0,10))
    if count == 0:
        maior = a[0]
        menor = a[0]
    if maior < a[count]:
        maior = a[count]
    if menor > a[count]:
        menor = a[count]
numbers = (a[0],a[1],a[2],a[3],a[4])
print('The tupla:')
for count in range(0,5):
    print(numbers[count], end=' ')

print(f'\nThe largest number is {maior}')
print(f'the smallest number is {menor}')