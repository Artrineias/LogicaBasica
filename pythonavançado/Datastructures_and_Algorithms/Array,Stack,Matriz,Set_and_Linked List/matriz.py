from random import randint
def Matriz_(coluna:int,linha:int):
    matriz = []
    for i in range(0,coluna,1):
        lin = []
        for j in range(0,linha,1):
            lin.append(randint(0,9))
        matriz.append(lin)
    return matriz

def Print_Matriz(matriz):
    coluna= len(matriz)
    linha= len(matriz[0])
    for i in range(0,coluna,1):
        for j in range(0,linha,1):
            print(f" {matriz[i][j]} ",end="")
        print('')

if __name__=="__main__":
    matriz = Matriz_(3,3)
    Print_Matriz(matriz)
    print(matriz)