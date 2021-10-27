jogador = {}
goals = []
jogador["name"] = input("Player's name:")
matches = int(input(f"how many matches did {jogador['name']} play?"))
total = 0
for i in range(0,matches):
    goals.append(int(input(f"how many goals in match {i}:")))
    total += goals[i]
jogador['goals'] = goals
jogador["total"] = total
print("-="*15)
print(jogador)
print("-="*15)
for k,v in jogador.items():
    print(f"The field {k} has the value {v}")
print("-="*15)
print(f"the player {jogador['name']} played {matches} matches")
for i in range(0,len(goals)):
    print(f'    =>In match {i} the player scored {goals[i]} goals')
print(f'it was a total of {jogador["total"]} goals')
