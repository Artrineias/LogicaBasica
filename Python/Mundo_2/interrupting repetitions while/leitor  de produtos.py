first = soma = count = 0
while True: 
    product = input("Product's Name: ")
    value = float(input('Product Value: '))
    first += 1
    soma += value
    if value > 1000:
        count += 1
    if first == 1:
        base = value
        name = product
    else:
        if base > value :
            base = value
            name = product
    end = ' '
    while end not in 'YN':
        end = input('want to continue:(Y/N)').upper()
    if end == 'N':
        print(f'The purchase total was {soma}')
        print(f'The quantity of products with a value above 1000 is {count}')
        print(f'The product with the lowest value was {name} costing {base}')
        break
