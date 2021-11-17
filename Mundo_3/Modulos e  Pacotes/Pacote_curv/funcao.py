from Pacote_curv import Moeda
def metade (n,moeda=False):
    if moeda:
        return Moeda.conversor(n/2)
    else:
        return n/2
def dobro(n,moeda=False):
    if moeda:
        return Moeda.conversor(n*2)
    else:
        return n*2


def aumento(n,p,moeda=False):
    if moeda:
        return Moeda.conversor(n-(n*(p/100)))
    else:
        return n+(n*(p/100))


def diminuir(n,p,moeda=False):
    if moeda:
        return Moeda.conversor(n-(n*(p/100)))
        
    else:
        return n-(n*(p/100))


def numero(n,moeda=False):
    if moeda:
        return Moeda.conversor(n)
    else:
        return n
