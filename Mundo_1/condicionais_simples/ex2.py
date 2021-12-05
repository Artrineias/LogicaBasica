velocidade = int(input('Insira a velocidade do carro: '))

if velocidade <= 80:
    print('Ainda dentro dos limite.')
else:
    multa = (velocidade-80)*7
    print('Veiculo ultrapasso o limite de velocidade.')
    print('A multa a ser paga vai ser de {}'.format(multa))

