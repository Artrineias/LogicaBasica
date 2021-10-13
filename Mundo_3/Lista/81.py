lista = []
while True:
    lista.append(int(input("Type a number:")))
    desição = input("Do you want to continue?(Y/N) ").upper()
    if desição == "N":
        break
print("-="*15)
print(f"you typed {len(lista)} numbers")
lista.sort(reverse=True)
print(f"Those in the list in descending order is {lista}")
if 5 in lista:
    print("The value 5 is part of the list.")
else:
    print("The value 5 is not part of the list.")