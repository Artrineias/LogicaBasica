def reader (mgs):
    n = input(mgs)
    while n.isdigit() == False:
        print("\033[0;31mERROR!!! Enter a whole number will count.\033[m")
        n = input("Enter a number: ")
    valor = int(n)
    return(valor)


n = reader("Enter a number: ")
print(f"You just typed the number {n}")