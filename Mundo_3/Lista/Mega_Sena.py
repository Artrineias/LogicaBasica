from random import randint
todas =[]
jogo = []
g = int(input("jogos: ")) 
for c in range(0,g):
    for a in range(0,6):
        jogo.append(randint(1,60))
    todas.append(jogo[:])
    jogo.clear()

for c in range(0,g):
    print(f"Jogo {c+1}: {todas[c]}")