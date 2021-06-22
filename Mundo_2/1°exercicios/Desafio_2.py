
numero = int(input('Digite um numero: '))
print('''Escolha o padrão numerico: 
[1] conversor para binario.
[2] conversor para octal.
[3] conversor para hexadecimal''')
opção = int(input('Sua escolha: '))
if opção == 1:
    print('O numero {} é {} em binario'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O numero {} é {} em octal'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('O numero {} é {} em hexadecimal'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida.')
