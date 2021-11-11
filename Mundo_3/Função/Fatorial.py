def fatorial(num,show=False):
    """
    -> Calcula o fatorial de um numero.
    :param num:O numero a ser calculado.
    :Param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um numero
    
    """
    count = fatorial = 1
    while count < num:
        if show == True:
            print(count,end=" X ")
        count += 1
        fatorial *= count
    if show == True:
        print(count,end=" = ")
    
    print(fatorial)


fatorial(5)
help(fatorial)