fix = {}
dados = []
f = ida = 0
while True:
    fix["name"] = input("Name:")
    fix["sex"] = input("Sex:").upper()
    while fix["sex"] not in "MF":
        del fix["sex"]
        print("Error, please just type M or F.")
        fix["sex"] = input("Sex:").upper()
    fix["age"] = int(input("Age:"))
    dados.append(fix.copy())
    ida += fix["age"] 
    while True:    
        decicao = input("Want to continue:").upper()
        if decicao in "NY":
            break
        print("Error, please just type N or Y")
    if decicao == "N":
        break    
media = ida/(len(dados))
print("-="*30)
print(f"A) Everyone has {len(dados)} registered people")
print(f"B) The average age is {media}")
print("C) The women registered were: ",end="")
for i in dados:
    if i["sex"] == "F":
        print(f"{i['name']}",end="")
        f += 1 
if f == 0:
    print("none")
else:
    print("")
print("D) List of people who are above average age:")
for i in dados:
    if i["age"] > media:
        print("->   ",end="")
        for k,v in i.items():
            print(f"{k} : {v};",end=" ")
        print("")

