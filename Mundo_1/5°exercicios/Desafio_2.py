n = int(input('digite um numero de 4 digitos: '))

print('A unidade do numero {} é {}'.format(n,n//1 % 10))
print('A dezena do numero {} é {}'.format(n,n//10 % 10))
print('A centena do numero {} é {}'.format(n,n//100 % 10))
print('A milhar do numero {} é {}'.format(n,n//1000 % 10))
