import datetime
year = int(input('Digite o ano o qual quer ser verificado:'))
if year == 0:
    year = 2021
criterion_1 = year % 4
criterion_2 = year % 100
criterion_3 = year % 400

if criterion_1 == 0 and criterion_2 != 0 or criterion_3 == 0:
    print('O ano é bissexto!!!')
else:
    print('o ano não é bissexto!!!')
