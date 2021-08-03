numero = int(input('Digite um numero:'))
for x in range(1,numero+1,1):
    resto = numero%(x/2)
    if resto == 0:
        print('{}\033[93m'.format(x),end="")
    else:
        print('{}\033[91m'.format(x),end="")