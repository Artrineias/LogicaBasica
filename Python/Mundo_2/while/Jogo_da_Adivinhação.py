import os
from random import randrange
from time import sleep
c = 1
os.system('clear')or None
print('Veja se você consegui acertar o valor escolido na maquina')
while(c == 1):
    pc = randrange(10)
    player = int(input('Numero(0 a 9): '))
    if pc == player:
        os.system('clear')or None
        print('você acertou!!!')
    else:
        os.system('clear')or None
        print('você errou!!!')
    print('Quer tentar denovo?')
    quebra = input('Digite S de sim e N se não: ').upper()
    if quebra == 'S':
        print('Ok...')
        sleep(2)
        os.system('clear')or None
    elif quebra == 'N':
        c = c - 1
        os.system('clear')or None
    else:
        print('valor invalido!!!')
        sleep(2)
        os.system('clear')or None