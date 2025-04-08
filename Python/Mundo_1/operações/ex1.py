
a = int(input('Type the number A:'))
b = int(input('Type the number B:'))

a1 = a - b
a2 = a + b
# soma e subtração são executados atraves de + e -
a3 = a / b
# a divisão é feita com esse / sinal
a4 = a // b
'''nesse caso a // faz a divisão sem virgula '''
a5 = a ** b
'''potencia é executada com '''
a6 = a * b
'''a multiplicação é executada *'''
a7 = a % b
'''aqui a % da o valor do resto da divisão'''
a8 = a ** (1/2)
a9 = b ** (1/2)
'''a raizes pode ser executada atravez da potencia de 1/2,1/3,1/4,...,1/n'''

print('Basic python operations:')
print('Sum:{}\n Subtraction:{}\n Division:{:.3f}'.format(a2, a1, a3))
print('Multiplication: {}\n Potentiation: {}\n Division '
      'without comma: {} '.format(a6, a5, a4))
print('Rest of the division: {}\n Root of A: {:.3f}\n Root of B:{:.3f}'.format(a7, a8, a9))
