import datetime
print('To be verified the categor you are in, you must inform the birth date. ')
date = int(input('Birth Date: '))
age = int(datetime.date.today().year) - date

if age <= 9:
    print('You are Little.')
elif age > 9 and age <= 14:
    print('You are Infant.')
elif age > 14 and age <= 19:
    print('You are Júnior.')
elif age > 19 and age <= 25:
    print('You are Senior.')
else:
    print('You are Master.')
