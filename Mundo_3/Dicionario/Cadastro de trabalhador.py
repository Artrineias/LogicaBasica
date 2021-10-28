trabalhadores = {}
trabalhadores["name"] = input("Name: ")
trabalhadores["age"]= 2020 - (int(input("Year of birth: ")))
trabalhadores["ctps"]= int(input("CTPS(0 doesn't have): "))
if trabalhadores["ctps"]!= 0:
    trabalhadores["hiring"] = int(input("Year of hiring: "))
    trabalhadores["salary"] = float(input("Salary: "))
    trabalhadores["retirement"] = trabalhadores["age"]+(35-(2020-trabalhadores["hiring"]))
for k,v in trabalhadores.items():
    if k == "name":
        print(f"-The {k} is {v}.")
    elif k == "age":
        print(f"-Your {k} is {v}.")
    elif k == "ctps":
        if v != 0:
            print(f"-Your {k} is {v}.")
        else:
            print("-This person doesn't ctps.")
    elif k == "hiring":
        print(f"-Your {k} was  in {v}.") 
    elif k == "salary":
        print(f"-Your {k} is R${v}")
    elif k == "retirement":
        print(f"-This person will only {k} with {v} age.")
