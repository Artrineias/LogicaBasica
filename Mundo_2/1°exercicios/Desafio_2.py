
number = int(input('Enter a number: '))
print('''choose the numerical pattern: 
[1] convert to binary.
[2] convert to octal.
[3] convert to hexadecimal''')
option = int(input('your choice: '))
if option == 1:
    print('The number {} is {} in binary'.format(number, bin(number)[2:]))
elif option == 2:
    print('The number {} is {} in octal'.format(number, oct(number)[2:]))
elif option == 3:
    print('The number {} is {} in hexadecimal'.format(number, hex(number)[2:]))
else:
    print('Invalid option.')
