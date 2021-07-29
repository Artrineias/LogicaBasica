print('Para saber se você tem que se alistar ou não esse ano.')
year = int(input('Digite o seu ano de nascimento:'))
age = 2021 - year
if age == 18:
    print('You is of military service age!!!')
elif age > 18:
    print('You are past military service age!!!')
else:
    print('You are still {} years old until military service.'.format((age-18)*(-1)))
    print('teste')
