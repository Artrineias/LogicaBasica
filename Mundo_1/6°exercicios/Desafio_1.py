import random
print('Tente advinha o numero que a maquina "pensou".\n')
number_user = int(input('Digite um numero de 0 a 5: '))
number_pc = random.randrange(6)
if number_pc == number_user:
    print('-----------------------\n')
    print('Você a certo o numero!!\n')
    print('-----------------------')
else:
    print('Você errou o numero!!')
    print('O valor da maquina era {} você falho ser humano.'.format(number_pc))
