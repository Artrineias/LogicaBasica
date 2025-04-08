while True:
    print('='*35)
    number = int(input('De qual numero da tabuada você quer? '))
    print('='*35)
    if number < 0:
        break
    for count in range(0,11,1):
        multi = number * count
        print(f'{number}x{count} = {multi}')
