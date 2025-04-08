lista = list()
for count in range(0,5):
    number = int(input("Type a number: "))
    if count == 0 or  number > lista[-1]:
        lista.append(number)
        print("The last position in the list.")
    else:
        pos = 0
        while pos < len(lista):
            if number <= lista[pos]:
                lista.insert(pos,number)
                print(f"The position in the list is {pos}.")
                break
            pos += 1
print(f"The value entered were {lista}")