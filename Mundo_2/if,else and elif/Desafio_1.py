print('Para fazer o pedido do emprestimo é preciso passar algumas informações.')
valor_do_imovel = float(input('Digite o valor do imovel: '))
salario = float(input('Digite o valor do salario mensal do comprador: '))
tempo = float(input('Digite em quantos anos vai ser parcelado o valor: '))

valor_mensal = valor_do_imovel / (tempo*12)
salario_30 = salario*0.3
if valor_mensal <= salario_30:
    print('O emprestimo foi aceito.')
else:
    print('O emprestimo foi negado')