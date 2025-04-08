
import os
cont = 1
soma = 0
count = 0
while cont== 1:
    os.system('clear')or None
    number = int(input('''(to stop the execution type 999)Type a number:'''))
    if number==999:
        cont = 0
    elif number < 0:
        print('Only positive numbers!!!')
    else:
        soma += number 
        count += 1

print('A soma dos numeros digitados foi {}'.format(soma))
print('O total de numeros digitados foi {}'.format(count))