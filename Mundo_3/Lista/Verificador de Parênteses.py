lista = input("escreva algo:")
a = 0 
for c in range(0,len(lista)):
    if lista[c] == "(":
        a +=1 
    elif lista[c] == ")":
        a -=1

if a == 0:
    print("sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")