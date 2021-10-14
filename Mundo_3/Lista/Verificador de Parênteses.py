lista = input("Enter the expression:")
a = 0 
for c in range(0,len(lista)):
    if lista[c] == "(":
        a +=1 
    elif lista[c] == ")":
        a -=1

if a == 0:
    print("Your expression is valid!!!")
else:
    print("Your expression is invalid!!!")