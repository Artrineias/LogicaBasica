n = int(input('Digite a quantidade de casa da seguencia de fibonacci que você quer ver:'))
contador = 0
base = 1
conta = 0
print('F = 0',end='')
while n >= conta:
    conta += 1
    valor_a = contador
    contador += base
    print('→{}'.format(contador),end='')
    base = valor_a
print("→fim")
    

    