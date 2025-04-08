from collections import namedtuple
from genericpath import isdir
from typing import List
import os


def fatorial(n:int)-> int:
    #caso base
    if n== 1:
        return 1
    return n* fatorial(n - 1)


Caixa = namedtuple("Caixa","tem_chave")

def encontra_caixa(caixas:List[Caixa],index:int = 0) -> Caixa:
    if len(caixas)<= index:
        return Caixa[False]
    caixa = caixas[index]
    print(f"Buscando chave na caixa de indice {index}")
    if caixa .tem_chave:
        return caixa
    index += 1
    return encontra_caixa(caixas,index)

if __name__== "__main__":
    caixas: List[Caixa] = [
        Caixa(False),Caixa(False),Caixa(False),
        Caixa(False),Caixa(False),Caixa(False)
        ,Caixa(False),Caixa(False),Caixa(True)
    ]

    #print(fatorial(995))
    #caminho = "/home/artrinias/Documents/codigo"
    #escanear_pastas(caminho)
    #apenas no windos...


def escanear_pastas(pasta_inicial, pasta = '',nivel = 0):
    caminho = os.path.join(pasta_inicial,pasta)
    if not os.path.isdir(caminho):
        return
    
    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        print('\t'*nivel,'>',arquivo)
        escanear_pastas(caminho,pasta,nivel + 1)

