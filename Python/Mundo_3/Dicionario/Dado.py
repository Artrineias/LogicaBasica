from random import randint
player = {}
a =0
for c in range(0,4):
    player[f"{c+1}°"] = randint(0,6)
    print(f'{c+1}°player {player[f"{c+1}°"]}')
print("Ranking of player:")
for i in sorted(player, key = player.get,reverse=True):
    a += 1
    print(f'{a}°place: {i}player with value {player[i]}')