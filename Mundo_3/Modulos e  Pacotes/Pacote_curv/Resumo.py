from Pacote_curv import funcao
from Pacote_curv import Verificador
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