def cont(i,f,p):
    print("=-"*25)
    if i < f:    
        print(f"Contagem de {i} ate {f} de {p} em {p}")
        for x in range(i,f+1,p):
            print(f"{x}..",end="")
        print("Fim")
        print("=-"*25)
    if i > f:
        print(f"Contagem de {i} ate {f} de {p} em {p}")
        for x in range(i,f-1,-p):
            print(f"{x}..",end="")
        print("Fim")
        print("=-"*25)


cont(0,10,1)
cont(10,0,2)
cont((int(input("init:"))),(int(input("fim:"))),(int(input("passou:"))))