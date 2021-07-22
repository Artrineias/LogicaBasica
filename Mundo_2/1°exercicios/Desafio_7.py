print('Give the value of the measurements of the sides.')
t_1 = float(input('1°side:'))
t_2 = float(input('2°side:'))
t_3 = float(input('3°side:'))
if t_1 < t_2 + t_3 and t_3 < t_2 + t_1 and t_2 < t_1 + t_3:
    print('This triangle exists!!!')
    if t_1 == t_2 and t_1 == t_3 and t_2 == t_3:
        print('equilatero')
    elif t_1 != t_3 and t_3 != t_2 and t_1 != t_2:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('This triangle does not exists!!!')
