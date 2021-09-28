table =('Atlético-MG',	'Palmeiras','Fortaleza','Flamengo','Bragantino'
,'Corinthians','Internacional','Fluminense','Athletico-PR','Cuiabá',
'Ceará','Atlético-GO','São Paulo','Juventude','América-MG',
'Santos','Bahia','Grêmio','Sport','Chapecoense')
print('(A) Only the top 5')
print('(B) The last 4 of the table')
print('(C) Team listed in alphabetical order')
print('(D) In what position is Corinthians')
choice = ' '
while choice not in 'ABCD':
    choice =input('Which alternative do you want(A,B,C,D):').upper()
if choice == 'A':
    for count in range(0,5):
        print(f'{count+1}°{table[count]}')

elif choice == 'B':
    for count in range(16,20):
        print(f'{count+1}°{table[count]}')
elif choice =='C':
    alfa = sorted(table)
    for count in range(0,20):
        print(f'{count+1}°{alfa[count]}')
else:
    for count in range(0,20):
        checker =table[count].find('Corinthians')
        if checker == 0:
             number = count
    print(f'{table[number]} is in position {number + 1} of the table')