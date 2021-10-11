from typing import Counter


lista = []
decision = 0
while True:    
    
    while True:
        if decision == 0:
            value =int(input("Enter a value: "))
        
        if value in lista:
            value = int(input("To this value in the list, type another value: "))
            decision = 1
        elif value not in lista:
            lista.append(value)
            decision = 0
            break

    decision = input("Want to Continue(Y/N): ").upper()
    if decision == "N":
        break
    elif decision == "Y" :
        a = []