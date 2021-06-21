print('Para calcular o aumento é necessario informa o salario atual.')
wage = int(input('Digite o salario atual:'))

if 1250 < wage:
    wage_10 = wage * 0.1
    print('O aumento foi de {} e o salario ficaria assim {}'.format(
        wage_10, wage+wage_10))
else:
    wage_15 = wage * 0.15
    print('O aumento foi de {} e o salario ficaria assim {}'.format(
        wage_15, wage+wage_15))
