from time import sleep 


def cont(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"contagem de {i} ate {f} de {p}  em {p}")
    sleep(1)
    if i < f:
        count = i
        while count<= f:
            print(f"{count}",end="->",flush=True)
            sleep(0.5)
            count += p
        print("END")
    else:
        count = i
        while count >= f:
            print(f"{count}",end="->",flush=True)
            sleep(0.5)
            count -= p
        print("END")


cont(0,10,1)
print("=-"*25)
cont(10,0,2)
print("=-"*25)
cont((int(input("Start:"))),(int(input("End:"))),(int(input("Passed on:"))))