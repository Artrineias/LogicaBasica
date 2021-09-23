from random import randrange
import os
count = 0
os.system('clear')or None
while True:
    print('=-'*10)
    print('Even or Odd')
    print('=-'*10)
    user = int(input('type a integer:'))
    print('=-'*10)
    user_caract = input('Choose even or odd:').upper()
    print('=-'*10)
    os.system('clear')or None
    pc = randrange(0,10)
    sum = pc + user
    rest = sum % 2
    if rest == 0:
        if user_caract == 'EVEN':
            print('=-'*6)
            print('User Won!!!')
            print('=-'*6)
            print('The pc played {} and the user {} the total was {}'.format(pc,user,sum))
        elif user_caract == 'ODD':
            print('=-'*6)
            print('Pc won!!!')
            print('=-'*6)
            print('The pc played {} and the user {} the total was {}'.format(pc,user,sum))
            print('The user won {} matches'.format(count))
            break
    elif rest != 0:
        if user_caract == 'ODD':
            print('=-'*6)
            print('User Won!!!')
            print('=-'*6)
            print('The pc played {} and the user {} the total was {}'.format(pc,user,sum))
        elif user_caract == 'EVEN':
            print('=-'*6)
            print('Pc won!!!')
            print('=-'*6)
            print('The pc played {} and the user {} the total was {}'.format(pc,user,sum))
            print('The user won {} matches'.format(count))
            break
    count += 1 