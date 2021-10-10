lista = []
for count in range(0,5):
    lista.append(int(input(f"Enter a Value For Position {count}:")))
smaller = lista[0]
larger = lista[0]
position_smaller= []
position_larger = []
for position,count in enumerate(lista): 
    if smaller >= count :
        if smaller > count:    
            position_smaller.clear()
        smaller = lista[position]
        position_smaller.append(position)
    if larger <= count :
        if larger < count:
            position_larger.clear()
        larger = lista[position]
        position_larger.append(position)
print("=-"*30)
print(f"You entered the {lista} values")
print(f"The largest values ​​entered was {larger} in positions ",end="")
for count in (position_larger):
    print(f"{count}...",end=" ")
print("")
print(f"The smallest values ​​entered was {smaller} in positions ",end="")
for count in (position_smaller):
    print(f"{count}...",end=" ")
print("")