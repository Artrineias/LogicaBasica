long_number = ('zero','one','two','three','four','five','six','seven','eight','nine','ten',
'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')
number = int(input('Enter a number between 0 and 20:'))

while number >= 20 or number < 0:
    number = int(input('type again (0 to 20):'))

print(f'the number {number} by extension is {long_number[number]}')