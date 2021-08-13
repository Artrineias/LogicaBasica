import os
from time import sleep
c = 1

while (c == 1):
    os.system('clear')or None
    sexo = input('Difite o seu sexo: ').upper()
    if sexo == 'M' or sexo == 'F':
        c = c - 1
        os.system('clear')or None
        print('Dado salvo!!!')
        sleep(3)
        os.system('clear')or None 
    else:
        os.system('clear')or None
        print('Dado invalido!!!')
        sleep(3)
            