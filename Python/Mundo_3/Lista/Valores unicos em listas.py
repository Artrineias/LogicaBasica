lista = list()
while True:    
    value =int(input("Enter a value: "))
        
    if value not in lista:
        lista.append(value)
        print("Successfully added value...")
    else:
        print("Duplicate value will not be added to the list.")
    
    decision = input("Want to Continue(Y/N): ").upper()
    if decision == "N":
        break
    elif decision == "Y" :
        b = []
print("-="*20)
lista.sort()
print(f"You entered these values ​​{lista}")