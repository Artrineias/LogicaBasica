
def name(name=""):
    while True:
        name = input('Name: ').strip()
        try:
            int(name)
        except KeyboardInterrupt:
            return '<desconhecido>'
        except ValueError:
            return name

        else:
            print('Erro!!!')
            continue
    


def age(age=""):
    while True:
        age = input('Age:')
        try:
            int(age)
        except ValueError:
            print('Erro!!!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return age


def verificaçãoage(age):
    try:
        int(age)
    except ValueError:
        return False
    else:
        return True


def formatador(mgs):
    print(f"{mgs}".center(30))


def traço(tamanho):
    print('-'*tamanho)

