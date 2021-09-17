import os
from time import sleep
c = 1

while (c == 1):
    os.system('clear')or None
    sexo = input('Digite o seu sexo(M = Masculino e F = Feminino): ').upper()
    if sexo == 'M' or sexo == 'F':
        c = c - 1
        os.system('clear')or None
        print('Dado salvo!!!')
        sleep(1)
        os.system('clear')or None 
    else:
        os.system('clear')or None
        print('Dado invalido!!!')
        sleep(3)
            