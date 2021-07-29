from random import randrange
from time import sleep
print('''-+-+-+-Vamo jogar Pedra,Papel e Tesoura-+-+-+-
Papel[0]
Pedra[1]
Tesoura[2]''')
escolha = int(input('Escolha: '))
escolha_pc = randrange(0,3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if escolha == 1 and escolha_pc == 2:
    print('-='*11)
    print("Pedra venceu")
    print("Você ganho da maquina")
    print('-='*11)
elif escolha == 1 and escolha_pc == 0:
    print('--'*11)
    print('Papel venceu')
    print("Você perdeu para a maquina")
    print('--'*11)
elif escolha == 1 and escolha_pc == 1:
    print('=='*11)
    print('---Você empataram---')
    print('=='*11)

elif escolha == 0 and escolha_pc == 1:
    print('-='*11)
    print('Papel venceu')
    print("Você ganho da maquina")
    print('-='*11)
elif escolha == 0 and escolha_pc == 2:
    print('--'*11)
    print('Tesoura venceu')
    print("Você perdeu para a maquina")
    print('--'*11)
elif escolha == 0 and escolha_pc == 0:
    print('=='*11)
    print('Você empataram')
    print('=='*11)

elif escolha == 2 and escolha_pc == 0:
    print('-='*11)
    print('Tesoura venceu')
    print("Você ganho da maquina")
    print('-='*11)
elif escolha == 2 and escolha_pc == 1:
    print('--'*11)
    print('Pedra venceu')
    print("Você perdeu para a maquina")
    print('--'*11)
elif escolha == 2 and escolha_pc == 2:
    print('=='*11)
    print('---Você empataram---')
    print('=='*11)
else:
    print("Opção invalida!!!")
