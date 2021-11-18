def leiaint(mgs):
    while True:    
        num = input(mgs).replace('-', '').replace('+', '').strip()
        c = 0

        try:
            int(num)
        except ValueError:
            c = 1
            print("Erro!!!")
        except KeyboardInterrupt:
            num = 0

        if c == 0:
            break
    return num

def leiafloat(mgs):
    while True:
        num = input(mgs).replace(',','.').replace('-', '').replace('+', '').strip()
        c = 0
        
        try:
            float(num)
        except ValueError:
            c = 1
            print("Erro!!!")
        except KeyboardInterrupt:
            num = 0
        
        if c == 0:
            break
    return num


i = leiaint("Type a number: ")
r = leiafloat("Type a number: ")