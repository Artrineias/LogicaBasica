from random import randint
todas =[]
jogo = []
g = int(input("How many games?: ")) 
for c in range(0,g):
    for a in range(0,6):
        jogo.append(randint(1,60))
    todas.append(jogo[:])
    jogo.clear()
print("-="*20)
for c in range(0,g):
    print(f"{c+1}°match : {todas[c]}")
print("-="*20)    