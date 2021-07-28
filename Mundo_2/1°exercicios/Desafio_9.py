product = float(input('enter the product value:'))
print('Payment options:\n 1° cash/check:10% discount'
      '\n 2° cash on the card:5% discount'
      '\n 3° up to 2x on the card:formal price'
      '\n 4° 3x or more on the card:20% interest')
option = int(input('Enter payment option number: '))

if option == 1:
    value = product-(product*0.1)
    print(value)
elif option == 2:
    value = product-(product*0.05)
    print(value)
elif option == 3:
    value = product
    print(value)
elif option == 4:
    x = int(input('how many times:'))
    if x >= 3:
        value =product + product*0.2
        value_2 = value/ x
        print('The installment to be paid is {} and value total amount is {}'.format(
        value_2, value))
    else:
        print('You entered an invalid option!!!')
else:
    print('You entered an invalid option!!!')