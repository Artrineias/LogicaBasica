
def reader(p,g):
    if p == "":
        p = "<Unknown>"
    
    if g == "" or (g.isnumeric()) == False:
        g = "0"
    print(f"Player {p} scored {g} goal(s) in the championship.")


#main
p = input("player: ")
g = input("Goal(s): ")
reader(p,g)
