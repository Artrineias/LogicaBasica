print('De o valor das medidas dos lados.')
t_1 = float(input('\033[0;31m1°lado:'))
t_2 = float(input('\033[0;33m2°lado:'))
t_3 = float(input('\033[0;32m3°lado:'))

if t_1 < t_2 + t_3 and t_3 < t_2 + t_1 and t_2 < t_1 + t_3:
    print('\033[0;30;42mEsse triangulo existe!!!\033[m')
else:
    print('\033[0;30;41mEsse triangulo não existe!!!\033[m')
