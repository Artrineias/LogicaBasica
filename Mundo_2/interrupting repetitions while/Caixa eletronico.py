value = int(input('Value: '))
one_hundred = twenty = ten = one = 0
while True:
    if value >= 100:
        one_hundred += 1
        value -= 100

    if value >= 20 and value < 100:
        twenty += 1
        value -= 20

    if value >= 10 and value < 50:
        ten += 1
        value -= 10

    if value >= 1 and value < 10:
        one += 1
        value -= 1

    if value == 0:
        break
print('=+'*30)
print(f'The number of ballots of 100 is {one_hundred}')
print(f'The number of ballots of 20 is {twenty}')
print(f'The number of ballots of 10 is {ten}')
print(f'The number of ballots of 1 is {one}')
print('=+'*30)