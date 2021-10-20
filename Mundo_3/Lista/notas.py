name = []
nota = []
c = b = 0
while True:
    
    name.append(input("Enter a name: "))
    nota.append(float(input("1°note: ")))
    nota.append(float(input("2°note: ")))
    nota.append((nota[0]+nota[1])/2)
    name.append(nota[:])
    nota.clear()
    
    decision = input("Want to continion: ").upper()
    if decision == "N":
        break

print("-="*25)
print("N.o   Name       Average" )
print("-"*25)
while b < (len(name)/2):
    print(f"{b: <6}{name[c]: <11}{name[c+1][2]}")
    b += 1
    c +=2
print("-"*25)
a = 0
while a != 999:
    a = int(input("Show a student's grade: "))
    if a <= b :
        if a == 0:
            print(f"The grades of {name[a*2]} is {name[(a*2)+1][0]},{name[(a*2)+1][1]}")
        elif a%2 == 0:
            print(f"The grades of {name[a*2]} is {name[(a*2)+1][0]},{name[(a*2)+1][1]}")
        else:
            print(f"The grades of {name[a*2]} is {name[(a*2)+1][0]},{name[(a*2)+1][1]}")