number = [' ',' ',' ',' ']
for count in range(0,4):
    number[count] = int(input('Type number:'))
numbers = (number[0],number[1],number[2],number[3])
nine = even = 0
for count in range(0,4):
    if numbers[count]==3:
        three = 0
        if three != count:
            three = count
            print(f'The value 3 appeared in the {three + 1}th position.')
    else:
        print('The value 3 does not appear at all.')

    if numbers[count] == 9:
        nine += 1
    
    if numbers[count]%2 == 0:
        print(f'The value of even numbers entered was {count}.')

if nine!=0:     
    print(f'The value 9 appeared {nine} times.')
else:
    print(f'The value 9 does not appear once.') 