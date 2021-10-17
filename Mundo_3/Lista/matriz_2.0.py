matriz = []
linha_1 = []
linha_2 = []
linha_3 = []
soma_p = soma_t = maior = 0
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
print("=-"* 15)
for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j]%2 == 0:
            soma_p += matriz[i][j]
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    
    if maior < matriz[1][c]:
        maior = matriz[1][c]

for c in range(0,3):
    soma_t+= matriz[c][2]
print(f"The sum of even values ​​is {soma_p}")
print(f"The sum of the values ​​in the third column is {soma_t}")
print(f"The largest value in the second line is {maior}")