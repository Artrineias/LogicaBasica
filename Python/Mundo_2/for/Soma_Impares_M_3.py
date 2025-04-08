sum = 0
cont = 0
for number in range(1,501,2):
    resto = number%3
    if resto == 0:
        sum = number + sum
        cont = cont +1
print("\nO valor de numeros somados foi esse {} e a soma total foi essa {}".format(cont,sum))