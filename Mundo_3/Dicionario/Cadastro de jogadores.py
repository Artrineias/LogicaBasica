
jogadores = {}
jogadores["goals"] = []
jogadores["total"] = 0
time = []
while True:
    jogadores["name"] = input("Name: ")
    jogadores["watches"] = int(input(f"how many matches did {jogadores['name']} play? "))
    for i in range(0,jogadores["watches"]):
        jogadores["goals"].append(int(input(f"{i}°game:")))
        jogadores["total"] += jogadores["goals"][i]
       