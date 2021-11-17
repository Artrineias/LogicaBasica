def analise(mgs):
    while True:
        n = input(mgs).replace(',','.').strip()
        if n.isalpha() or n =="":
            print(f'ERRO!!!\"{n}\" is a price Invalid!')
        else:
            break
    return float(n)