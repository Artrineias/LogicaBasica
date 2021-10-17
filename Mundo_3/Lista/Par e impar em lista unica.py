lista = []
even = []
odd = []
for c in range(0,7):
    lista.append(int(input(f"{c+1}°Type a number: ")))

for c in range(0,7):
    if lista[c]%2 == 0:
        even.append(lista[c])

for c in range(0,7):
        if lista[c]%2 != 0:
            odd.append(lista[c])
print("=-"*30)
print(f"The even values ​​entered were: {even}")
print(f"The odd values ​​entered were: {odd}")