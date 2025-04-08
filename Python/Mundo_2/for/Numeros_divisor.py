valor = int(input("Digite um numero: "))
y = 0
for x in range(1,valor+1,1):
    cont = valor%x 
    if cont == 0:
        print("\033[1;33m {} ".format(x),end=" ")
        y = y+1
    else:
        print("\033[1;31m {} ".format(x),end=" ")
if y <= 2:
    print("\nO numero {} é primo pois so é divisivel por {} numeros.".format(valor,y))
else:
    print("\nO numero {} não é primo por que tem {} divisores.".format(valor,y))
