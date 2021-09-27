number = [' ',' ',' ',' ']
for count in range(0,4):
    number[count] = int(input('Type number:'))
numbers = (number[0],number[1],number[2],number[3])
nine = even = 0
for count in range(0,4):
    if numbers[count]==3:
        three = count
    if numbers[count] == 9:
        nine += 1 
    if numbers[count]%2 == 0:
        even += 1
print(f'The value 9 appeared {nine} times.')
print(f'The value 3 appeared in the {three + 1}th position.')
print(f'The value of even numbers entered was {even}.')