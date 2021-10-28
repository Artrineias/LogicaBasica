fix = {}
dados = []
f = ida = 0
while True:
    fix["name"] = input("Name:")
    fix["sex"] = input("Sex:").upper()
    while fix["sex"] not in "MF":
        del fix["sex"]
        print("Error, please just type Y or N.")
        fix["sex"] = input("Sex:").upper()
    fix["age"] = int(input("Age:"))
    dados.append(fix.copy())
    ida += fix["age"] 
    decicao = input("Want to continue:").upper()
    del fix["name"]
    del fix["age"]
    del fix["sex"]
    if decicao == "N":
        break    
media = ida/(len(dados))
print("-="*30)
print(f"A) Everyone has {len(dados)} registered people")
print(f"B) The average age is {media}")
print("C) The women registered were: ",end="")
for i in range(0,len(dados)):
    if dados[i]["sex"] == "F":
        print(f"{dados[i]['name']}",end="")
        f += 1 
if f == 0:
    print("none")
else:
    print("")
print("D) List of people who are above average age:")
for i in range(0,len(dados)):
    if dados[i]["age"] > media:
        print("->   ",end="")
        for k,v in dados[i].items():
            print(f"{k} : {v};",end=" ")
        print("")

