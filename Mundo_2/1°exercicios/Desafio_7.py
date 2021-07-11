print('De o valor das medidas dos lados.')
t_1 = float(input('1°lado:'))
t_2 = float(input('2°lado:'))
t_3 = float(input('3°lado:'))

if t_1 < t_2 + t_3 and t_3 < t_2 + t_1 and t_2 < t_1 + t_3:
    print('Esse triangulo   existe!!!')
else:
    print('Esse triangulo não existe!!!')
