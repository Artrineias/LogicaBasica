even = []
odd = []
number =[]
c = 0
while True: 
    number.append(int(input("Type a number: ")))
    
    if number[c]%2 == 0:
        even.append(number[c])
    elif number[c]%2 != 0:
        odd.append(number[c])

    decision = input("Want to continue(Y/N): ").upper()
    if decision == "N":
        break

    c += 1
print(f"The complete list is {number}")
print(f"The list of even numbers is {even}")
print(f"The list of even numbers is {odd}")