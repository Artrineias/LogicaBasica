from random import randint
lista = []
def soma(lista):
    s = 0  
    for x in range(0,5):
        if lista[x]%2 == 0:
            s += lista[x]
    print(f"Somando os valores pares de {lista} temos {s}")
    print("")


def sorteio(lista):
    print(f"Sorteando 5 valores da lista : ",end="")

    for x in range(0,5):
        a = randint(0,10)
        print(f"{a}",end=" ")
        lista.append(a)
    print("Pronto!")
    soma(lista)




sorteio(lista)