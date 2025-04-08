main = []
personal_data = []
while True:
    personal_data.append(input("Name: "))
    personal_data.append(int(input("Weight: ")))
    
    if len(main) == 0:
        smaller = bigger = personal_data[1]
    else:
        if smaller > personal_data[1]:
            smaller = personal_data[1]
        if bigger < personal_data[1]:
            bigger = personal_data[1]
    
    main.append(personal_data[:])
    personal_data.clear()

    desicion = input("Want to continuon: ").upper()
    if desicion == "N":
        break

print(f"In all, you registered {len(main)} people.")

print(f"The greatest weight was {bigger}. The person with this staff are ",end="")
for c in range(0,len(main)):
    if main[c][1]== bigger:
        print(f"{main[c][0]}",end="")
print("")

print(f"The smallest weight was {smaller}. The person with this person are ",end="")
for c in range(0,len(main)):
    if main[c][1]== smaller:
        print(f"{main[c][0]}",end="")
print("")
