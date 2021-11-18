from Pacote_curv import funcao
def mostra (n,a,d,c):
    tam = 26+len(str(n))
    print("-"*tam)
    print("SUMMARY".center(tam))
    print("-"*tam)
    print(f"Price analyzed:  \t{funcao.numero(n,c)}")
    print(f"Double the price:\t{funcao.dobro(n,c)}")
    print(f"Half-price: \t\t{funcao.metade(n,c)}")
    print(f"{a}% increase: \t\t{funcao.aumento(n,a,c)}")
    print(f"{d}% reduction: \t\t{funcao.diminuir(n,d,c)}")
    print("-"*tam)

def analise(mgs):
    while True:
        n = input(mgs).replace(',','.').strip()
        if n.isalpha() or n =="":
            print(f'ERRO!!!\"{n}\" is a price Invalid!')
        else:
            break
    return float(n)

def conversor (num):
    return (f'R$ {num:.2f}').replace('.',',')