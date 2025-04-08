termo= int(input('primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo + (10-1) * razão
for x in range(termo,decimo + razão,razão):
    print(" {} ".format(x),end="→")
print(' ACABOU')