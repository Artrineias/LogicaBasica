fator = int(input('Digite o numero para calcular o fatorial: '))
print('{}! = '.format(fator), end="")
print('{} '.format(fator), end="")
fatorial = fator
while (fator!=1 or fator<1):
    fator = fator - 1
    fatorial = fatorial * fator 
    print('X {} '.format(fator), end="")
print(f"= {fatorial}")