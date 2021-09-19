count = sun = key = 0
while (key == 0):
    number = float(input('Digite um numero:'))
    answer = input('Quer adicionar mais numeros? ').upper()
    sun += number
    count += 1
    if count == 1:
        larger = smaller = number
    if number > larger:
        larger = number
    elif number < smaller:
        smaller = number   
    if 'S' == answer:
        key = 0
    elif 'N' == answer:
        key = 1
        average = sun/count
        print('O maior numero foi {} e o menor foi {} dos {} numeros digitados.'.format(larger,smaller,count))
        print('A media dos valores digitados é {}'.format(average))
    else:
        print('invalid option!!!')
        key = 1 
    