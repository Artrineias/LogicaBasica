sum = 0
cont = 0
for request in range(1,7,1):
    number= int(input('Digite o {}°valor : '.format(request)))
    if number%2 == 0:
        sum = number + sum
        cont = cont + 1
print('Você informou {} numeros pares e soma desses numeros é {}'.format(cont,sum))