soma_p = soma_t = maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Enter the number for Column {j} X Row {i}:"))
print("=-"* 15)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]",end="")
        if matriz[i][j]%2 == 0:
            soma_p += matriz[i][j]
    print("")
print("=-"* 15)
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