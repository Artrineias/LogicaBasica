count = soma = 0
while True:
    number = int(input('type a number(999 to end the program):'))
    if number == 999:
        print(f'The sum of {count} number  is {soma}. ')
        break
    count += 1
    soma += number