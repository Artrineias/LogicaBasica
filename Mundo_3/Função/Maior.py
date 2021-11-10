from time import sleep

def maior(*num):
    count = maior = 0
    for x in num:
        print(x,end=" ",flush=True)
        sleep(0.1)
        if count == 0:
            maior = x
        else:
            if x> maior:
                maior = x
        count += 1
        
    print(f"{len(num)} values ​​were given in total.")
    print(f"The highest value entered was {maior}")


def espaço():
    print("-="*30)

espaço()
maior(2,9,4,5,7,1)
espaço()
maior(4,7,0)
espaço()
maior(1,2)
espaço()
maior(6)
espaço()
maior(18,68,15,43,73,26,39,11,15,43,91,68,6,20,30,5,62,25,22,72,14,80,32,95,37,4,13,80,83,13,44)
espaço()
maior()