first = float(input('Digite o primeiro valor:'))
second = float(input('Digite o segundo valor:'))
manipulador = 6
while (5!=manipulador):
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    manipulador = int(input('Digite o numero para escolher a proxima ação: '))
    if manipulador == 1:
        soma = first + second
        print('A soma de {} e {} é {}'.format(first,second,soma))
    elif manipulador == 2:
        multiplicador = first * second
        print('A multiplicação do numero {} e {} é {}'.format(first,second,multiplicador))
    elif manipulador == 3:
        if first > second: 
            print('O numero {} é maior que {}'.format(first,second))
        elif second > first:
            print('O numero {} é maior que {}'.format(second,first))
        elif first == second:
            print('Os numeros são iguais.')
    elif manipulador == 4:
        first = float(input('Digite o primeiro valor:'))
        second = float(input('Digite o segundo valor:'))
    elif manipulador == 5:
        print('Finalizado.')
    else:
        print('Operação invalida.')