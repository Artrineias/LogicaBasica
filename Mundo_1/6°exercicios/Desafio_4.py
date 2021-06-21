distance = float(input('Qual a distancia da viagem pretendida: '))

if distance <= 200:
    print('O valor a ser pago é {:.2f}'.format(distance*0.50))
else:
    print('O valor a ser pago é {:.2f}'.format(distance*0.45))

