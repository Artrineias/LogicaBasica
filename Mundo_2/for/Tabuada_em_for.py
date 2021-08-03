number = int(input('Digite um numero para gerar a tabuada: '))
for cont in range(0,11,1):
    print("{} X {} = {}".format(number,cont,number*cont))