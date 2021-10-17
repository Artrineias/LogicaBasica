matriz = []
linha_1 = []
linha_2 = []
linha_3 = []

for c in range(0,3):
    linha_1.append(int(input(f"Enter the number for Column {c+1} X Row 1:")))
for c in range(0,3):
    linha_2.append(int(input(f"Enter the number for Column {c+1} X Row 2:")))
for c in range(0,3):
    linha_3.append(int(input(f"Enter the number for Column {c+1} X Row 3:")))

matriz.append(linha_1)
matriz.append(linha_2)
matriz.append(linha_3)
print("=-"* 15)
for i in range(0,3):
    for j in range(0,3):
        print(f"[ {matriz[i][j]} ]",end="")
    print("")

