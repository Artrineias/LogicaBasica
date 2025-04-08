def leiaint(mgs):
    while True:    

        try:
            num = int(input(mgs).replace('-', '').replace('+', '').strip())
        except (ValueError, TypeError):
            print("Erro!!!")
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return num


def leiafloat(mgs):
    while True:
        try:
            num = float(input(mgs).replace('-', '').replace('+', '').strip())
        except (ValueError, TypeError):
            print("Erro!!!")
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return num


i = leiaint("Type a number I: ")
r = leiafloat("Type a number R: ")
print(f"O numero inteiro digitado é {i} e o numero real digitado é {r}")