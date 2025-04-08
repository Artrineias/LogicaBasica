import os
os.system('clear')or None
W_s = i = man = 0
while True:
    age = int(input('Age: '))
    gender = ' ' 
    while gender not in 'MW':
        gender = input('gender(M/W): ').upper()
    if age < 20 and gender == 'W':
            W_s += 1 
    if age > 18:
        i += 1
    if gender == 'M':
       man += 1
    a = ' '
    while a not in 'YN':
        a = input('want to continue(Y/N):').upper()
    if a == 'Y':
        os.system('clear')or None
    elif a == 'N':
        print(f'The number of women under 20 years old added was {W_s}')
        print(f'The number of Men added to the lysate was {man}')
        print(f'The number of people of legal age is {i}')
        break