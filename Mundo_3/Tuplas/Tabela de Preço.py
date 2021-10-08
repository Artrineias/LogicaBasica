lista = ('Lapís',1.75,'Borracha',2.00,'Caderno',15.90,
'Estojo',25.00,'Transferido',4.20,'Compasso',9.99,'Mochila'
,120.32,'Canetas',22.30,'livro',34.90)


for count in range(0,17,2):
    print(f'{lista[count]}',end =" ")
    print('.'*(15 - len(lista[count])),end =" ")
    print(f'R$',end=" ")
    print(' '*(7 - len(str(lista[count+1]))),end=" ")
    print(f'{lista[count+1]}')