
day = int(input('Enter to how many of day the car was rented: '))
km = float(input('Enter the distance covered in this time in Km:'))

print('The value to be paid is {}'.format(day*60 + km*0.15))
