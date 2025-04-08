ficha = []
while True:
    
    name = input("Enter a name: ")
    nota_1 = float(input("1°note: "))
    nota_2 = float(input("2°note: "))
    media =  (nota_2 + nota_1)/2
    ficha.append([name,[nota_1,nota_2],media])
    
    decision = input("Want to continion: ").upper()
    if decision == "N":
        break

print("-="*25)
print(f'{"N.o":<4}   {"Name":<10}{"Average":>8}' )
print("-"*25)
for i,j in enumerate(ficha):
    print(f"{i:<4}{j[0]:<10}{j[2]:>8.1f}")
print("-"*25)
while True:
    opc = int(input("Mostrar notas de qual aluno?(999 interrompe):"))
    if opc== 999:
        print("End...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas do {ficha[opc][0]} são {ficha[opc][1]}.")