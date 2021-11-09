def cont(i,f,p):
    print("=-"*25)
    if i < f:    
        print(f"Counting from {i} to {f} from {p} at {p}")
        for x in range(i,f+1,p):
            print(f"{x}..",end="")
        print("End")
        print("=-"*25)
    if i > f:
        print(f"Counting from {i} to {f} from {p} at {p}")
        for x in range(i,f-1,-p):
            print(f"{x}...",end="")
        print("End")
        print("=-"*25)


cont(0,10,1)
cont(10,0,2)
cont((int(input("Start:"))),(int(input("End:"))),(int(input("Passed on:"))))