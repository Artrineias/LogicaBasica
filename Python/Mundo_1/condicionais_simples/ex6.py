print('Digite três numeros diferentes entre si.')
number_1 = float(input('Digite o 1°numero:'))
number_2 = float(input('Digite o 2°numero:'))
number_3 = float(input('Digite o 3°numero:'))

maior = number_1

if number_2 > number_1 and number_2 > number_3:
    maior = number_2
if number_3 > number_1 and number_3 > number_2:
    maior = number_3

print('O maior numero é {:.2f}'.format(maior))
menor = number_1

if number_2 < number_1 and number_2 < number_3:
    menor = number_2
if number_3 < number_1 and number_3 < number_2:
    menor = number_3
print('O menor numero é {:.2f}'.format(menor))
