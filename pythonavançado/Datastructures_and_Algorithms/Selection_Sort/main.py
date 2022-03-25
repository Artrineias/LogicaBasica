from random import randint,randrange
def gerador(tamanho):
    lista = []
    for i in range(0,tamanho,1):
        lista.append(randint(0,99))
    return lista

def gerador_str(tamanho):
    lista = []
    for i in range(0,tamanho,1):
        lista.append(chr(randint(ord("a"),ord("z"))))
    return lista

def menor_elemento(lista,x,y=0):
    menor = lista[y]
    for i in range(y,x,1):
        if menor >= lista[i]:
            menor = lista[i]
            pos = i
    return pos


def ordenador (lista):
    nova_lista = []
    print(lista)
    for j in range(0,len(lista),1): 
        posição = menor_elemento(lista,len(lista))
        nova_lista.append(lista.pop(posição))
        
    return nova_lista


def swap(lista):
    print(lista)
    for j in range(0,len(lista),1):
        pos = menor_elemento(lista,len(lista),j)
        swapPositions(lista,j,pos)
    return lista


def swapPositions(list, inicio, menor): 
    list[inicio],list[menor] = list[menor],list[inicio]
    return list

if __name__=="__main__":
    print(swap(gerador(10)))
    print(ordenador(gerador(10)))
    print(swap(gerador_str(10)))
    print(ordenador(gerador_str(10)))
