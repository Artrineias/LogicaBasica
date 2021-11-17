import funcao
import Moeda

num = float(input("Type a number:"))

print(f"Half of {Moeda.conversor(num)} is {Moeda.conversor(funcao.metade(num))}")
print(f"Double {Moeda.conversor(num)} is {Moeda.conversor(funcao.dobro(num))}")
print(f"The 10% increase, we have {funcao.aumento(num,10)}")
print(f"The 10% decrease, we have {funcao.diminuir(num,13)}")