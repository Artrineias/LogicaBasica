valor = int(input("Digite um numero: "))

for x in range(1,valor+1,1):
    cont = 0
    for y in range(1,x+1,1):
        
        resto = x%y
        if resto == 0:
            cont= cont + 1
        else:
            cont = cont 
    if cont <= 2:
        print("\033[1;33m {} ".format(x),end=" ")
    else:
        print("\033[1;31m {} ".format(x),end=" ")