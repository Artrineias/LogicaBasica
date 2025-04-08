
jogadores = {}
team = []
while True:
    jogadores["name"] = input("Name: ")
    jogadores["watches"] = int(input(f"how many matches did {jogadores['name']} play? "))
    jogadores["goals"] = []
    jogadores["total"] = 0
    for i in range(0,jogadores["watches"]):
        jogadores["goals"].append(int(input(f"{i+1}°game:")))
        jogadores["total"] += jogadores["goals"][i]
    
    team.append(jogadores.copy())
    jogadores.clear()
    desicao = input("Want to continue: ").upper()
    while desicao not in "YN":
        print("Type N or Y...")
        desicao = input("Want to continue: ").upper()
    if desicao == "N":
        break
print("=-"*20)
print(f'{"cod":<4}{"name":<10}{"goals":<10}{"total"}')
print("-"*30)
l = []
for i,j in enumerate(team):
    print(f"{str(i):<4}"f"{str(j['name']):<10}"f"{str(j['goals']):<10}"f"{str(j['total'])}")
    l.append(i)
print("-"*30)
while True:    
    player = int(input("Shows which player's data (999 to exit): "))
    if player == 999:
        break
    while player not in l:
        print("Type the number of players...")
        player = int(input("Shows which player's data (999 to exit):"))
        if player == 999:
            break
    print(f'Player data {team[player]["name"]}')
    for i,j in enumerate(team[player]["goals"]):
        print(f"{i+1}°Game:{j}")
    if player == 999:
        break
