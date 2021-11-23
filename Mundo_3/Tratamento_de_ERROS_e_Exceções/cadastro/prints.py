def name(name=""):
    while True:
        name = input('Name: ').strip()
        if name == "":
            name = 1
        if verificaçãoname(name):
            break
    return name


def age(age=""):
    while True:
        age = input('Age: ')
        if verificaçãoage(age):
            break
    return age


def verificaçãoname(name):
    try:
        int(name)
    except ValueError:
        return True
    else:
        print('Erro!!!')
        return False


def verificaçãoage(age):
    try:
        int(age)
    except ValueError:
        print('Erro!!!')
        return False
    else:
        return True
