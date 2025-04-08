import os
for x in range(1,6,1):
    
    peso = float(input("peso da {}°pessoa:".format(x)))
    if x == 1:
        maior = peso
        menor = peso
    if maior > peso:
        maior = peso
    
    if menor < peso:
        menor = peso
    os.system('clear')or None
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))
