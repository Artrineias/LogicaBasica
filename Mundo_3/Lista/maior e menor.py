lista = []
for count in range(0,5):
    lista.append(int(input(f"Enter a Value For Position {count}:")))
smaller = larger = lista[0]

for position,count in enumerate(lista): 
    if smaller >= count :
        smaller = lista[position]
    if larger <= count :
        larger = lista[position]

print("=-"*30)
print(f"You entered the {lista} values")

print(f"The largest values ​​entered was {larger} in positions ",end="")
for count,j in enumerate(lista):
    if j == larger:
        print(f"{count}...",end=" ")
print("")

print(f"The smallest values ​​entered was {smaller} in positions ",end="")
for count,i in  enumerate(lista):
    if i == smaller:
        print(f"{count}...",end=" ")
print("")