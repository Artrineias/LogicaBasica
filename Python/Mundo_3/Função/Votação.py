def verificador (age):
    if age < 16:
        return("WITHHOLD")
    elif age >= 16 and age < 18 or age > 70:
        return("OPTIONAL")
    else:
        return("MANDATORY")

def age (year):
    age =  2021 - year
    return age


# Programa
year = int(input("Enter the year of birth: "))
print(f"At age {age(year)}, the vote is {verificador(age(year))}")