from datetime import date
import os 
atual = date.today().year
cont_M = 0
cont_m = 0
for x in range(1,8,1):
    os.system('clear')or None
    ano = int(input("Digite o ano de nascimento da {}°pessoa:".format(x)))
    idade = atual - ano
    if idade >= 18:
        cont_M = cont_M + 1
    else:
        cont_m = cont_m + 1
os.system('clear')or None
print("No todal tivemos {} pessoas menores de idade".format(cont_m))
print("E {} pessoas maiores de idade".format(cont_M))
