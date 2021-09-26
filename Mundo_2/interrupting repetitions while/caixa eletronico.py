print('what amount will be withdrawn')
value = float(input('Value:'))
one_hundred = 0
while True:
    if value > 100:
        one_hundred += 1
        value -= 100
    print(value)
    if value > 0:
        break