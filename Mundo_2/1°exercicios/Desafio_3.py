"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""
print('Enter two numbers.')
number_1 = int(input('1°number: '))
number_2 = int(input('2°number:'))
if number_1 == number_2:
    print('Não existe valor maior, os dois numeros são iguais.')
elif number_1 > number_2:
    print('O valor {} é maior que {}.'.format(number_1, number_2))
else:
    print('O valor {} é maior que {}.'.format(number_2, number_1))
