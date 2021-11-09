from random import randint
list = []
def sum(list):
    s = 0  
    for x in range(0,5):
        if list[x]%2 == 0:
            s += list[x]
    print(f"Adding the even values ​​of {list} we have {s}")
    print("")


def sortition(list):
    print(f"Drawing 5 values ​​from the list: ",end="")

    for x in range(0,5):
        a = randint(0,10)
        print(f"{a}",end=" ")
        list.append(a)
    print("Ready!")
    sum(list)




sortition(list)