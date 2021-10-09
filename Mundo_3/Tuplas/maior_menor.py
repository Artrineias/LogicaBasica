from random import randrange
numbers = (randrange(0,10),randrange(0,10),randrange(0,10),randrange(0,10),randrange(0,10))
for count in range(0,5):
    if count == 0:
        maior = numbers[0]
        menor = numbers[0]
    if maior < numbers[count]:
        maior = numbers[count]
    if menor > numbers[count]:
        menor = numbers[count]
print('The tupla:')
for count in range(0,5):
    print(numbers[count], end=' ')

print(f'\nThe largest number is {maior}')
print(f'the smallest number is {menor}')